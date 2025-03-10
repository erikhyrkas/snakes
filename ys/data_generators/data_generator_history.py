import random
from typing import Tuple

from ys.data_generators.util.generator_harness import generate_training_files_v2
from ys.data_generators.util.ollama_prompter import prompt_ollama

# Map of dates to descriptions
important_dates = {
    "4.5 billion years ago": "Formation of Earth",
    "4.4 billion years ago": "Oldest known zircon crystals (evidence of Earth's crust)",
    "4.1 billion years ago": "Hypothetical period of Late Heavy Bombardment",
    "3.8 billion years ago": "First evidence of life (stromatolites)",
    "3.5 billion years ago": "Cyanobacteria (oxygen-producing bacteria)",
    "3.0 billion years ago": "Formation of the first supercontinent (Vaalbara)",
    "2.7 billion years ago": "Oxygenation of Earth's atmosphere begins (Great Oxygenation Event)",
    "2.4 billion years ago": "Huronian glaciation (one of the first ice ages)",
    "2.0 billion years ago": "Formation of the supercontinent Columbia",
    "1.8 billion years ago": "Emergence of complex single-celled life (eukaryotes)",
    "1.6 billion years ago": "Formation of the supercontinent Rodinia",
    "1.2 billion years ago": "Emergence of multicellular life",
    "900 million years ago": "Cryogenian period (snowball Earth)",
    "750 million years ago": "Breakup of the supercontinent Rodinia",
    "600 million years ago": "Ediacaran biota (first complex multicellular life)",
    "540 million years ago": "Cambrian Explosion (diversification of life)",
    "485 million years ago": "Ordovician-Silurian extinction events",
    "450 million years ago": "First land plants",
    "400 million years ago": "First land vertebrates (amphibians)",
    "360 million years ago": "Devonian extinction event",
    "335 million years ago": "Formation of the supercontinent Pangaea",
    "300 million years ago": "Coal swamps and the evolution of reptiles",
    "250 million years ago": "Permian-Triassic extinction event (the Great Dying)",
    "230 million years ago": "First dinosaurs",
    "201 million years ago": "Triassic-Jurassic extinction event",
    "150 million years ago": "Age of the dinosaurs (Jurassic period)",
    "130 million years ago": "First flowering plants (angiosperms)",
    "100 million years ago": "Rise of the Cretaceous period, peak of dinosaurs",
    "65 million years ago": "Cretaceous-Paleogene extinction event (dinosaurs' extinction)",
    "50 million years ago": "Mammals begin to dominate the Earth",
    "25 million years ago": "Evolution of the first apes",
    "7 million years ago": "Divergence of the human and chimpanzee lineages",
    "4 million years ago": "Australopithecus (early human ancestors)",
    "2 million years ago": "Homo habilis (early human species)",
    "1.8 million years ago": "Homo erectus (more advanced early humans)",
    "1 million years ago": "Earliest use of fire by humans",
    "400,000 years ago": "Homo sapiens (early modern humans) emerge",
    "200,000 years ago": "Evolution of anatomically modern humans",
    "100,000 years ago": "Migration of modern humans out of Africa",
    "50,000 years ago": "Development of complex language and culture",
    "30,000 years ago": "Extinction of Neanderthals",
    "20,000 years ago": "Last Glacial Maximum (peak of the last Ice Age)",
    "12,000 years ago": "Beginning of the Holocene epoch (current geological epoch)",
    "11,000 BC": "End of the Ice Age and beginning of human civilization",
    "10,000 BC": "Agricultural revolution begins (Neolithic)",
    "8000 BC": "First permanent human settlements",
    "7000 BC": "Development of pottery in the Near East",
    "6000 BC": "Domestication of the horse",
    "5000 BC": "Early forms of writing in Mesopotamia",
    "4000 BC": "Establishment of the first cities in Sumer",
    "3500 BC": "Invention of the wheel in Mesopotamia",
    "3200 BC": "Unification of Upper and Lower Egypt",
    "2560 BC": "Construction of the Great Pyramid of Giza",
    "2400 BC": "Development of the Akkadian Empire",
    "2000 BC": "First use of bronze (Bronze Age)",
    "1800 BC": "Code of Hammurabi (ancient law code)",
    "1500 BC": "Aryan migration into India",
    "1200 BC": "Collapse of the Bronze Age civilizations",
    "1000 BC": "Rise of the Kingdom of Israel",
    "800 BC": "Foundation of Rome",
    "776 BC": "First Olympic Games in Greece",
    "500 BC": "Birth of Buddha",
    "490 BC": "Battle of Marathon (Greco-Persian Wars)",
    "480 BC": "Battle of Thermopylae (Greco-Persian Wars)",
    "431 BC": "Beginning of the Peloponnesian War",
    "323 BC": "Death of Alexander the Great",
    "221 BC": "Unification of China under the Qin Dynasty",
    "146 BC": "Destruction of Carthage in the Third Punic War",
    "44 BC": "Assassination of Julius Caesar",
    "27 BC": "Founding of the Roman Empire under Augustus",
    "79 AD": "Eruption of Mount Vesuvius (destruction of Pompeii)",
    "313 AD": "Edict of Milan (legalization of Christianity in Rome)",
    "476 AD": "Fall of the Western Roman Empire",
    "622 AD": "Hijra (migration of Muhammad to Medina)",
    "800 AD": "Coronation of Charlemagne as Holy Roman Emperor",
    "1066 AD": "Norman Conquest of England (Battle of Hastings)",
    "1215 AD": "Signing of the Magna Carta",
    "1347 AD": "Black Death begins in Europe",
    "1453 AD": "Fall of Constantinople (end of the Byzantine Empire)",
    "1492 AD": "Christopher Columbus lands in the Americas",
    "1517 AD": "Martin Luther's 95 Theses (start of the Protestant Reformation)",
    "1607 AD": "Establishment of Jamestown, Virginia",
    "1687 AD": "Publication of Newton's *Principia Mathematica*",
    "1776 AD": "Declaration of Independence (United States)",
    "1789 AD": "Start of the French Revolution",
    "1804 AD": "Napoleon crowns himself Emperor of France",
    "1865 AD": "End of the American Civil War",
    "1879 AD": "Invention of the light bulb by Thomas Edison",
    "1914 AD": "Start of World War I",
    "1917 AD": "Russian Revolution",
    "1929 AD": "Start of the Great Depression",
    "1939 AD": "Start of World War II",
    "1945 AD": "End of World War II (atomic bombs dropped on Hiroshima and Nagasaki)",
    "1963 AD": "Martin Luther King Jr.'s \"I Have a Dream\" speech",
    "1969 AD": "Apollo 11 moon landing",
    "1973 AD": "The oil crisis (OPEC oil embargo)",
    "1989 AD": "Fall of the Berlin Wall",
    "1991 AD": "Dissolution of the Soviet Union",
    "2001 AD": "September 11 attacks (start of the War on Terror)",
    "2008 AD": "Global financial crisis",
    "2016 AD": "The UK votes to leave the European Union (Brexit referendum)",
    "2020 AD": "COVID-19 pandemic begins",
}


def load_dates():
    """
    Shuffle and load the list of important dates.
    """
    dates = list(important_dates.items())
    random.shuffle(dates)
    return dates


def generate_event_prompt(date, description):
    prompt = (
        f"Write a script for a YouTube video that discusses the event: '{description}' that occurred around {date}. "
        f"Explain why it was significant, its impact, and how it fits into the broader timeline of history."
    )
    return prompt


def entry_generator() -> Tuple[str, str]:
    dates = load_dates()

    while True:
        for idx, (date, description) in enumerate(dates):
            prompt = generate_event_prompt(date, description)
            script = prompt_ollama(prompt)
            yield prompt, script

if __name__ == '__main__':
    generate_training_files_v2("generated-scripts", entry_generator)
