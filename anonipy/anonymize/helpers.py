from ..definitions import Entity

# =====================================
# Entity converters
# =====================================


def convert_spacy_to_entity(entity, label):
    return Entity(
        entity.text,
        entity.label_,
        entity.start_char,
        entity.end_char,
        label["type"],
        label["regex"] if "regex" in label else ".*",
    )
