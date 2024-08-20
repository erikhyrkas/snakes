import random

from ollama import generate

emotions = {
    "positive_emotions": ['happiness',
                          'excitement',
                          'love',
                          'satisfaction',
                          'trust',
                          'joy',
                          'gratitude',
                          'contentment',
                          'pride',
                          'optimism',
                          'hope', ],
    "negative_emotions": ['anger',
                          'disgust',
                          'fear',
                          'sadness',
                          'frustration',
                          'confusion',
                          'anxiety',
                          'loneliness',
                          'guilt',
                          'shame',
                          'envy',
                          'boredom'],
    "uncertain_emotions": ['surprise',
                           'neutrality',
                           'curiosity',
                           'anticipation',
                           'indifference']
}
subjects = ["the latest sci-fi movie", "a new book", 'a video', "a recent political event", "a new tech gadget",
            "a sports game last night"]


def generate_review(emotion, subject):
    prompt = (
        f"Imagine you just experienced {subject}. Write a review explaining how it made you feel {emotion}. "
        "Describe specific aspects or moments that particularly influenced your feelings."
    )
    response = generate('llama3.1', prompt)
    review = response['response'].strip()
    return review


def generate_prompt(subject, review, emotion):
    templates = [
        f'Identify the emotion expressed by the author in their review of {subject}:\n"{review}"\n<start>{emotion}<end>',
        f'What feeling does the following review convey about {subject}?\n"{review}"\n<start>{emotion}<end>',
        f'Guess the mood of the reviewer discussing this {subject}:\n"{review}"\n<start>{emotion}<end>',
        f'Considering the review below, what emotion was likely driving the reviewer’s thoughts on {subject}?\n"{review}"\n<start>{emotion}<end>',
        f'Analyze the following review and determine the emotional tone regarding {subject}:\n"{review}"\n<start>{emotion}<end>'
    ]

    chosen_template = random.choice(templates)
    return chosen_template


def sentiment_generator():
    sentiments = []
    for i in range(20):
        for category, emo_list in emotions.items():
            for emotion in emo_list:
                for subject in subjects:
                    review = generate_review(emotion, subject)
                    new_prompt = generate_prompt(subject, review, emotion)
                    print(f"{emotion} {subject}:\n{review}\n{new_prompt}")
                    sentiments.append(new_prompt)
        output_file = f'./training_data/llama-sentiment-{i}.md'
        with open(output_file, 'w', encoding="utf-8") as file:
            file.writelines(sentiments)


if __name__ == '__main__':
    sentiment_generator()
