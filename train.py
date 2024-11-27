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

    # I want to see if using varying lengths of short sequences will help solidify which words work together.
    # Basic ideas, like that "The" is generally followed by a noun, or that a noun is generally followed by a
    # verb or adverb. These exceptionally short sequences aren't useful for teaching it to remember long context,
    # but we'll slowly expand.
    #
    # My sequence and batch sizes are tuned to fit in memory, but aren't often a power of two. I found that it
    # really didn't have much impact on the speed of training, despite initially thinking that encouraging allocations
    # along memory boundaries and avoiding fragmentation might help. It might just be that things are too complex
    # to ever really fall along memory boundaries and that I'm always going to have some fragmentation.

    base_model_train(0.001, 3, 3700, 50, patience=5, training_folder=TRAIN_FOLDER,
                     use_validation_split=False)
    shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_16.bin")

    remove_scheduler_checkpoint()
    base_model_train(0.001, 5, 2048, 50, patience=5, training_folder=TRAIN_FOLDER,
                     use_validation_split=False)
    shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_16.bin")

    remove_scheduler_checkpoint()
    base_model_train(0.001, 4, 2700, 50, patience=5, training_folder=TRAIN_FOLDER,
                     use_validation_split=False)
    shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_16.bin")



    remove_scheduler_checkpoint()
    base_model_train(0.00025, 16, 680, 100, patience=5, training_folder=TRAIN_FOLDER,
                     use_validation_split=False)
    shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_16.bin")

    remove_scheduler_checkpoint()
    base_model_train(0.00025, 63, 170, 40, patience=5, training_folder=TRAIN_FOLDER,
                     use_validation_split=False)
    shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_64.bin")

    remove_scheduler_checkpoint()
    base_model_train(0.00025, 254, 42, 20, patience=10, training_folder=TRAIN_FOLDER,
                     use_validation_split=False)
    shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_256.bin")


    base_model_train(0.00025, 15, 680, 100, patience=5, training_folder=TRAIN_FOLDER,
                     use_validation_split=False)
    shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_16.bin")

    remove_scheduler_checkpoint()
    base_model_train(0.00025, 68, 170, 40, patience=5, training_folder=TRAIN_FOLDER,
                     use_validation_split=False)
    shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_64.bin")

    remove_scheduler_checkpoint()
    base_model_train(0.00025, 235, 42, 40, patience=10, training_folder=TRAIN_FOLDER,
                     use_validation_split=False)
    shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_256.bin")

    # remove_scheduler_checkpoint()
    # base_model_train(0.00025, 512, 32, 11, patience=10, training_folder=TRAIN_FOLDER,
    #                  use_validation_split=False)
    # shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_512.bin")
    #
    # remove_scheduler_checkpoint()
    # base_model_train(0.00025, 1024, 12, 10, patience=10, training_folder=TRAIN_FOLDER,
    #                  use_validation_split=False)
    # shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_1024.bin")
    #
    # remove_scheduler_checkpoint()
    # base_model_train(0.0001, 1024, 12, 10, patience=10, training_folder=TRAIN_FOLDER,
    #                  use_validation_split=False)
    # shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_1024_2.bin")
    #
    # remove_scheduler_checkpoint()
    # base_model_train(0.00008, 64, 256, 20, patience=5, training_folder=TRAIN_FOLDER,
    #                  use_validation_split=False)
    # shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_64_2.bin")
    #
    # remove_scheduler_checkpoint()
    # base_model_train(0.00008, 66, 256, 20, patience=5, training_folder=TRAIN_FOLDER,
    #                  use_validation_split=False)  # slightly different sequence length
    # shutil.copyfile(f"{get_base_path()}model/model_checkpoint.bin", f"{get_base_path()}model/model_checkpoint_64_3.bin")
