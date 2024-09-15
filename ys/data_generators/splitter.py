def split_file_by_sections(input_file, sections_per_file=100):
    try:
        base_file_name = input_file.split(".")[0]

        with open(f"./training_data/{input_file}", 'r') as file:
            content = file.read()

        # Split the content into sections while keeping the '<end>' tag with each section
        sections = content.split('<end>')
        sections = [section.strip() + '<end>' for section in sections if section.strip()]

        # Group sections into chunks of the desired size
        for i in range(0, len(sections), sections_per_file):
            chunk = sections[i:i + sections_per_file]
            output_file = f"./training_data/{base_file_name}_{i // sections_per_file}.md"
            with open(output_file, 'w') as out_file:
                out_file.write('\n'.join(chunk) + '\n')

            print(f"Written {len(chunk)} sections to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    input_file = 'llama-stories.md'
    split_file_by_sections(input_file)