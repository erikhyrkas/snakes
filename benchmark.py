import json
import os

from ys.inference.model_interface import ModelInterface


class CapitalWordFrequencyChecker:
    @staticmethod
    def check(response, frequency_threshold=0.1):
        """Check if capital word frequency meets a threshold."""
        words = response.split()
        capital_words = [word for word in words if word.isupper()]
        return (len(capital_words) / len(words)) >= frequency_threshold


class CapitalLettersEnglishChecker:
    @staticmethod
    def check(response):
        """Check if the response contains only capitalized words (English)."""
        return response.isupper()


class LowercaseLettersEnglishChecker:
    @staticmethod
    def check(response):
        """Check if the response contains only lowercase words (English)."""
        return response.islower()


class RepeatPromptChecker:
    @staticmethod
    def check(response, prompt):
        """Check if the response repeats the prompt before answering."""
        return response.startswith(prompt)


class TwoResponsesChecker:
    @staticmethod
    def check(response):
        """Check if two distinct responses are provided."""
        responses = response.split("\n\n")
        return len(responses) >= 2


class NumberPlaceholdersChecker:
    @staticmethod
    def check(response, required_placeholders=1):
        """Check if the required number of placeholders are in the response."""
        return response.count("[PLACEHOLDER]") == required_placeholders


class ConstrainedResponseChecker:
    @staticmethod
    def check(response, max_length=100):
        """Check if the response meets the constrained length."""
        return len(response) <= max_length


class JsonFormatChecker:
    @staticmethod
    def check(response):
        """Check if the response is a valid JSON."""
        try:
            json.loads(response)
            return True
        except json.JSONDecodeError:
            return False


class MultipleSectionsChecker:
    @staticmethod
    def check(response, required_sections=2):
        """Check if the response contains the required number of sections."""
        sections = response.split("\n\n")
        return len(sections) >= required_sections


class BulletListChecker:
    @staticmethod
    def check(response, required_bullets=3):
        """Check if the response contains the required number of bullet points."""
        bullet_points = response.count("* ")
        return bullet_points >= required_bullets


class HighlightedSectionsChecker:
    @staticmethod
    def check(response, required_highlighted_sections=2):
        """Check if the response contains highlighted sections (marked)."""
        return response.count("**") // 2 >= required_highlighted_sections


class TitleChecker:
    @staticmethod
    def check(response):
        """Check if the response starts with a title (assumed title-case or header)."""
        return response.split("\n", 1)[0].istitle()


class KeywordChecker:
    @staticmethod
    def check(response, keywords):
        """Check if all required keywords are present in the response."""
        return all(keyword in response for keyword in keywords)


class ForbiddenWordsChecker:
    @staticmethod
    def check(response, forbidden_words):
        """Check if no forbidden words are used in the response."""
        return all(word not in response for word in forbidden_words)


class KeywordFrequencyChecker:
    @staticmethod
    def check(response, keyword, frequency_threshold):
        """Check if a keyword appears with a specific frequency."""
        return response.count(keyword) >= frequency_threshold


class LetterFrequencyChecker:
    @staticmethod
    def check(response, letter, frequency_threshold):
        """Check if a letter appears with a specific frequency."""
        return response.count(letter) >= frequency_threshold


class ResponseLanguageChecker:
    @staticmethod
    def check(response, language="english"):
        """Check if the response is in the specified language."""
        return all(ord(c) < 128 for c in response)  # Assume English -- since we only train on english.


class NthParagraphFirstWordChecker:
    @staticmethod
    def check(response, nth_paragraph, first_word):
        """Check if the nth paragraph starts with the specified first word."""
        paragraphs = response.split("\n\n")
        return paragraphs[nth_paragraph].startswith(first_word)


class NumberParagraphsChecker:
    @staticmethod
    def check(response, required_paragraphs):
        """Check if the response has the required number of paragraphs."""
        paragraphs = response.split("\n\n")
        return len(paragraphs) == required_paragraphs


class NumberSentencesChecker:
    @staticmethod
    def check(response, required_sentences):
        """Check if the response has the required number of sentences."""
        sentences = response.split(". ")
        return len(sentences) == required_sentences


class EndChecker:
    @staticmethod
    def check(response, required_end="The end."):
        """Check if the response ends with a specific phrase."""
        return response.endswith(required_end)


class QuotationChecker:
    @staticmethod
    def check(response):
        """Check if the response contains a quotation (assumed marked by quotation marks)."""
        return '"' in response or '“' in response or '”' in response


class CommaChecker:
    @staticmethod
    def check(response):
        """Check if the response contains no commas."""
        return "," not in response


class NumberOfWordsChecker:
    @staticmethod
    def check(response, min_words=100, max_words=150):
        """Check if the response contains the right number of words."""
        word_count = len(response.split())
        return min_words <= word_count <= max_words


class PostscriptChecker:
    @staticmethod
    def check(response, postscript):
        """Check if the response ends with the required postscript."""
        return response.endswith(postscript)


# This is based on:
#
# @article{zhou2023instruction,
#   title={Instruction-Following Evaluation for Large Language Models},
#   author={Zhou, Jeffrey and Lu, Tianjian and Mishra, Swaroop and Brahma, Siddhartha and Basu, Sujoy and Luan, Yi and Zhou, Denny and Hou, Le},
#   journal={arXiv preprint arXiv:2311.07911},
#   year={2023}
# }
class IFEvalEvaluator:
    def __init__(self, model):
        self.model = model
        self.instruct_dict = {
            "change_case:capital_word_frequency": (
                CapitalWordFrequencyChecker.check, ["capital_frequency", "relation"]),
            "change_case:english_capital": (CapitalLettersEnglishChecker.check, []),
            "change_case:english_lowercase": (LowercaseLettersEnglishChecker.check, []),
            "combination:repeat_prompt": (RepeatPromptChecker.check, ["prompt_to_repeat"]),
            "combination:two_responses": (TwoResponsesChecker.check, []),
            "detectable_content:number_placeholders": (NumberPlaceholdersChecker.check, ["num_placeholders"]),
            "detectable_content:postscript": (PostscriptChecker.check, ["postscript"]),
            "detectable_format:constrained_response": (ConstrainedResponseChecker.check, ["max_length"]),
            "detectable_format:json_format": (JsonFormatChecker.check, []),
            "detectable_format:multiple_sections": (MultipleSectionsChecker.check, ["required_sections"]),
            "detectable_format:number_bullet_lists": (BulletListChecker.check, ["num_bullets"]),
            "detectable_format:number_highlighted_sections": (
                HighlightedSectionsChecker.check, ["required_highlighted_sections"]),
            "detectable_format:title": (TitleChecker.check, []),
            "keywords:existence": (KeywordChecker.check, ["keywords"]),
            "keywords:forbidden_words": (ForbiddenWordsChecker.check, ["forbidden_words"]),
            "keywords:frequency": (KeywordFrequencyChecker.check, ["keyword", "frequency_threshold"]),
            "keywords:letter_frequency": (LetterFrequencyChecker.check, ["letter", "frequency_threshold"]),
            "language:response_language": (ResponseLanguageChecker.check, ["language"]),
            "length_constraints:nth_paragraph_first_word": (
                NthParagraphFirstWordChecker.check, ["nth_paragraph", "first_word"]),
            "length_constraints:number_paragraphs": (NumberParagraphsChecker.check, ["required_paragraphs"]),
            "length_constraints:number_sentences": (NumberSentencesChecker.check, ["required_sentences"]),
            "length_constraints:number_words": (NumberOfWordsChecker.check, ["min_words", "max_words"]),
            "punctuation:no_comma": (CommaChecker.check, []),
            "startend:end_checker": (EndChecker.check, ["required_end"]),
            "startend:quotation": (QuotationChecker.check, []),
        }

    @staticmethod
    def filter_args(instruction, args):
        """Filter the args relevant for the given instruction based on instruct_dict."""
        checker_function, relevant_args = instruction
        return {k: v for k, v in args.items() if k in relevant_args}

    @staticmethod
    def prompt_format(record):
        """Formats the prompt from the IFEval dataset for model input."""
        return f"{record['prompt']}"

    def evaluate(self, path):
        """Evaluate the model using IFEval prompts and log results."""
        results = []
        total_correct = 0
        total_prompts = 0
        eval_records = []

        with open(path, 'r') as file:
            for line in file:
                data = json.loads(line)
                eval_records.append(data)

        for eval_record in eval_records:
            prompt = self.prompt_format(eval_record)
            print(f"Prompt: {prompt}")
            response = self.model.complete(prompt, 1.0, 128)
            print(f"Raw response: {response}")
            response = response.strip()

            is_following_instruction = self.verify_instruction(response, eval_record['instruction_id_list'],
                                                               eval_record['kwargs'])

            if is_following_instruction:
                print(f"Correct Response: {response}")
                total_correct += 1
            else:
                print(f"Incorrect Response: {response}")

            total_prompts += 1
            results.append({
                'prompt_key': eval_record['key'],
                'response': response,
                'correct': is_following_instruction
            })

        accuracy = total_correct / total_prompts if total_prompts > 0 else 0
        print(f"Overall Accuracy: {accuracy * 100:.2f}%")

        for result in results:
            status = "Correct" if result['correct'] else "Incorrect"
            print(f"Prompt Key: {result['prompt_key']}, Response: {result['response']}, {status}")

    def verify_instruction(self, response, instruction_list, eval_args):
        """Check if the response follows the instructions (e.g., no commas)."""
        for instruction in instruction_list:
            checker_function, relevant_args = self.instruct_dict.get(instruction, (None, []))
            if checker_function:
                filtered_args = self.filter_args((checker_function, relevant_args), eval_args)
                if not checker_function(response, **filtered_args):
                    return False
        return True


class MMLUProEvaluator:
    def __init__(self, model: ModelInterface):
        self.model = model

    @staticmethod
    def prompt_format_question_answer(question):
        options_text = "\n".join([f"{chr(65 + i)}. {opt}" for i, opt in enumerate(question['options'])])
        return f"Question: {question['question']}\n{options_text}\n<start>Answer: "

    @staticmethod
    def prompt_format_q_a(question):
        options_text = "\n".join([f"{chr(65 + i)}. {opt}" for i, opt in enumerate(question['options'])])
        return f"Q: {question['question']}\n{options_text}\n<start>A: "

    @staticmethod
    def prompt_format(question):
        options_text = "\n".join([f"{chr(65 + i)}. {opt}" for i, opt in enumerate(question['options'])])
        return f"{question['question']}\n{options_text}\n<start>"

    def evaluate(self, path):
        results = []
        total_correct = 0
        total_questions = 0
        dataset = []
        with open(path, 'r') as file:
            for line in file:
                question_data = json.loads(line)
                dataset.append(question_data)
        for question in dataset:
            prompt = self.prompt_format(question)
            print(f"Prompt: {prompt}")
            response = self.model.complete(prompt, 1.0, 128)
            print(f"Raw response: {response}")
            response = response.replace(prompt, '')
            response = response.strip()

            response = response.split('\n')[0].strip()  # only keep first line of text to ignore explanations.

            correct_answer_letter = chr(65 + question['answer_index'])  # Convert answer_index to A, B, C, etc.
            correct_answer_text = question['options'][question['answer_index']]  # Get the correct answer text
            correct_combined_1 = f"{correct_answer_letter}. {correct_answer_text}"  # Letter + text
            correct_combined_2 = f"{correct_answer_letter}: {correct_answer_text}"
            correct_combined_3 = f"{correct_answer_letter}, {correct_answer_text}"
            correct_combined_4 = f"{correct_answer_letter}; {correct_answer_text}"
            correct_combined_5 = f"{correct_answer_letter} ({correct_answer_text})"
            print(f"Expected response: {correct_combined_1}")
            # Normalize response to account for various possibilities
            response = response.strip().lower()

            # Check if the response matches any of the possible formats
            is_correct = (
                    response == correct_answer_letter.lower() or  # Single letter match
                    response == correct_answer_text.strip().lower() or  # Text match
                    response == correct_combined_1.strip().lower() or  # Letter + text match
                    response == correct_combined_2.strip().lower() or
                    response == correct_combined_3.strip().lower() or
                    response == correct_combined_4.strip().lower() or
                    response == correct_combined_5.strip().lower()
            )
            if is_correct:
                print(f"Correct Response: {response}")
            else:
                print(f"Incorrect Response: {response}")
            if is_correct:
                total_correct += 1
            total_questions += 1

            results.append({
                'question_id': question['question_id'],
                'response': response,
                'correct': is_correct
            })

        accuracy = total_correct / total_questions if total_questions > 0 else 0

        for result in results:
            status = "Correct" if result['correct'] else "Incorrect"
            print(f"Question ID: {result['question_id']}, Your Answer: {result['response']}, {status}")
        print(f"Overall Accuracy: {accuracy * 100:.2f}%")


def build_model_interface():
    base_path = os.getenv("YS_LLM_BASE_PATH", "./")

    model_path = f"{base_path}model/model.bin"
    if not os.path.isfile(model_path):
        model_path = f"{base_path}model/model_checkpoint.bin"

    tokenizer_path = f"{base_path}model/tokenizer.pkl"
    config_save_path = f"{base_path}model/model_config.json"
    if not os.path.exists(model_path):
        print("Did you forget to train the model?")
        return None
    if not os.path.exists(tokenizer_path):
        print("Did you forget to train the tokenizer?")
        return None

    print("Loading...")
    model_interface = ModelInterface(model_save_path=model_path, tokenizer_save_path=tokenizer_path,
                                     config_save_path=config_save_path)
    return model_interface


def evaluate_mmlu_pro(model_interface):
    evaluator = MMLUProEvaluator(model_interface)
    evaluator.evaluate("benchmark_data/mmlu-pro.jsonl")


def evaluate_if(model_interface):
    evaluator = IFEvalEvaluator(model_interface)
    evaluator.evaluate("benchmark_data/ifeval_input_data.jsonl")


def evaluate_snakes():
    model_interface = build_model_interface()
    evaluate_mmlu_pro(model_interface)
    evaluate_if(model_interface)


if __name__ == '__main__':
    evaluate_snakes()
