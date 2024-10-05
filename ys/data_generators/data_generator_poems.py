import os
import random
import time

from ys.data_generators.util.ollama_prompter import prompt_ollama


# a bunch of poems and songs


def main(count):
    record_number = 0
    output_file = f"./training_data/llama-song-poems-{count}.md"
    input_file = "./ys/data_generators/song_poem_themes.txt"
    fast_forwarding_count = 0
    if os.path.exists(output_file):
        return
    start_time = time.time()
    records_this_session = 0
    song_poem_prompt_choices = ["Write ",
                                "Compose ",
                                "Draft "
                                ]

    with (open(input_file, "r", encoding='utf-8') as prompts, open(output_file, "a", encoding='utf-8') as result_file):
        while next_input := prompts.readline():
            if record_number < fast_forwarding_count:
                record_number += 1
                continue
            theme = next_input.strip()
            poem_or_song = random.choice(["poem", "song"])
            if poem_or_song == "poem":
                poem_system_prompt = (
                    f"Compose a short poem based on the theme '{theme}'. The poem should be limited to four to six "
                    "lines. Focus on creating vivid imagery and emotion while keeping the language simple and clear. "
                    "Incorporate elements like rhyme, rhythm, or alliteration as appropriate, but ensure the poem "
                    "remains coherent and thematically consistent. Avoid overly complex vocabulary or convoluted "
                    "metaphors. Conclude with a line that leaves a lasting impression or encapsulates the theme "
                    "effectively. Only respond with the poem.\n"
                )
                prompt = poem_system_prompt
            else:
                song_system_prompt = (
                    f"Write a short song lyric centered around the theme '{theme}'. The lyric should consist of two "
                    "to four verses, each with four to six lines. Emphasize a clear, catchy chorus that captures the "
                    "essence of the theme. The verses should tell a story or convey emotions related to the theme, "
                    "using simple and relatable language. Incorporate rhyme and rhythm to enhance the musicality of "
                    "the lyrics. Avoid complex language or abstract metaphors. The chorus should be memorable and "
                    "summarize the main message or feeling of the song. Only respond with the song.\n"
                )
                prompt = song_system_prompt
            creation = prompt_ollama(prompt)
            user_prompt = random.choice(song_poem_prompt_choices)
            full_result = f"{user_prompt}a {poem_or_song} about {theme}.<start>{creation}<end>\n"
            print("Full Result:", full_result)
            result_file.write(full_result)
            result_file.flush()
            record_number += 1
            records_this_session += 1
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"-----{record_number}: {int(elapsed_time / records_this_session)} seconds "
                  f" ({int(elapsed_time / 60)} minutes)-----")


if __name__ == '__main__':
    for i in range(20):
        main(i)
