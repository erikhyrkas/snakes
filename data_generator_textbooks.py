import yaml
import os

import ollama


# Assuming generate function is defined as follows:
def generate(prompt: str) -> str:
    response = ollama.generate('llama3.1', prompt)
    result = response['response'].strip()
    print(f"{prompt}:\n{result}")
    return result


# Function to create Markdown formatted text
def format_md_title(text, level=1):
    return f"{'#' * level} {text}\n"


def generate_section_content(book_title, chapter_name, section_name):
    prompt = (
        f"Write detailed content for the section titled '{section_name}' in the chapter '{chapter_name}' "
        f"of the book '{book_title}'. Use a conversational, easy-to-understand tone, and include definitions of any "
        f"jargon used. Your response should only be the section content."
    )
    return generate(prompt)


def generate_chapter_intro(book_title, chapter_name, sections):
    section_list = ', '.join(sections)
    prompt = (
        f"Write an engaging introduction for the chapter '{chapter_name}' in the book '{book_title}'. "
        f"The chapter includes the following sections: {section_list}. Set the stage for these sections and outline "
        f"their importance. Your response should only be the introduction."
    )
    return generate(prompt)


def generate_chapter_summary(book_title, chapter_name, section_list):
    prompt = (
        f"Write a conclusion section for the chapter '{chapter_name}' in the book '{book_title}'. The chapter "
        f"included the following sections: {section_list}. Summarize the key takeaways from the chapter, reinforcing "
        f"the main points covered in each section. Your response should only be the chapter conclusion."
    )
    return generate(prompt)


def generate_book_intro(book_title, part_names):
    part_list = ', '.join(part_names)
    prompt = (
        f"Write an introduction for the book '{book_title}'. "
        f"The book covers the following key topics: {part_list}. Provide context for the reader and highlight the "
        f"significance of these topics. Your response should only be the introduction."
    )
    return generate(prompt)


def generate_book_content(output_dir, book, book_number):
    output_file = os.path.join(output_dir, f"llama-textbook-{book_number}.md")
    if os.path.exists(output_file):
        print(f"Output file '{output_file}' already exists. Skipping.")
        return

    # Extract part names for the book introduction
    part_names = [part['part_name'] for part in book.get('parts', [])]

    # Start the Markdown content with the title page
    book_title = book['title']
    md_content = format_md_title(book_title, level=1)

    # Generate book introduction with key topics
    book_intro = generate_book_intro(book_title, part_names)
    md_content += book_intro + "\n\n"

    part_number = 1

    for part in book.get('parts', []):
        md_content += format_md_title(part['part_name'], level=2)

        chapter_number = 1

        for chapter in part.get('chapters', []):
            chapter_name = chapter['chapter_name']
            md_content += format_md_title(chapter_name, level=3)

            sections = chapter.get('sections', [])
            section_contents = []
            for section in sections:
                section_name = section
                # Generate content for each section with context
                section_content = generate_section_content(book_title, chapter_name, section_name)
                section_contents.append(section_content)
                md_content += format_md_title(section_name, level=4)
                md_content += section_content + "\n\n"

            # Generate chapter introduction (except for the final chapter)
            if chapter_number < len(part['chapters']):
                chapter_intro = generate_chapter_intro(book_title, chapter_name, sections)
                md_content = md_content.replace(f"{format_md_title(chapter_name, level=3)}",
                                                f"{format_md_title(chapter_name, level=3)}\n{chapter_intro}\n\n", 1)

            # Generate chapter summary (except for the final chapter)
            if chapter_number < len(part['chapters']):
                chapter_summary = generate_chapter_summary(book_title, chapter_name, sections)
                md_content += format_md_title("Chapter Summary", level=4)
                md_content += chapter_summary + "\n\n"

            chapter_number += 1

        part_number += 1

    md_content = f"Write a textbook entitled '{book_title}'.<start>{md_content}<end>"

    # Write to a Markdown file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)


def textbook_generator():
    # Load the YAML file
    with open('.\\textbook.yaml', 'r') as file:
        textbooks = yaml.safe_load(file)

    # Ensure the output directory exists
    output_dir = '.\\training_data\\'
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through the textbooks and generate content for each
    for i, book in enumerate(textbooks['books'], start=1):
        generate_book_content(output_dir, book, i)

    print("Book generation complete.")


if __name__ == '__main__':
    textbook_generator()
