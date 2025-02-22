import os
import shutil
import sys

from ys.training.trainer import get_base_path, train_or_load_tokenizer, base_model_train


def cleanup_old_bins(remove_tokenizer=False, clear_cache=False):
    print("Cleaning up...")
    base_path = get_base_path()
    if os.path.exists(f"{base_path}model/scheduler_checkpoint.bin"):
        os.remove(f"{base_path}model/scheduler_checkpoint.bin")
    if os.path.exists(f"{base_path}model/optimizer_checkpoint.bin"):
        os.remove(f"{base_path}model/optimizer_checkpoint.bin")
    if os.path.exists(f"{base_path}model/model_checkpoint.bin"):
        os.remove(f"{base_path}model/model_checkpoint.bin")
    if os.path.exists(f"{base_path}model/model.bin"):
        os.remove(f"{base_path}model/model.bin")
    if os.path.exists(f"{base_path}model/model_config.json"):
        os.remove(f"{base_path}model/model_config.json")
    if clear_cache and os.path.exists(f"{base_path}model/fine_tuning"):
        os.removedirs(f"{base_path}model/fine_tuning")
    if clear_cache and os.path.exists(f"{base_path}model/training_data_cache"):
        os.removedirs(f"{base_path}model/training_data_cache")
    if clear_cache and os.path.exists(f"{base_path}model/validation_data_cache"):
        os.removedirs(f"{base_path}model/validation_data_cache")
    if remove_tokenizer and os.path.exists(f"{base_path}model/tokenizer.pkl"):
        os.remove(f"{base_path}model/tokenizer.pkl")


def warmed_up() -> bool:
    base_path = get_base_path()
    return os.path.exists(f"{base_path}model/model.bin")


def remove_scheduler_checkpoint():
    base_path = get_base_path()
    if os.path.exists(f"{base_path}model/scheduler_checkpoint.bin"):
        os.remove(f"{base_path}model/scheduler_checkpoint.bin")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "clean":
        if len(sys.argv) > 2 and sys.argv[2] == "all":
            cleanup_old_bins(True, True)
        else:
            cleanup_old_bins()

    train_or_load_tokenizer("training_data")

    TRAIN_FOLDER = "training_data"

    remove_scheduler_checkpoint()
    base_model_train(0.00005, 16, 256, 100, patience=2, training_folder=TRAIN_FOLDER,
                     use_validation_split=False)
    shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_16.bin")

    remove_scheduler_checkpoint()
    base_model_train(0.00001, 250, 16, 5, patience=2, training_folder=TRAIN_FOLDER,
                     use_validation_split=True)
    shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_250.bin")

