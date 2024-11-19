from enum import Enum

class ImportOption(Enum):
    SAMPLE_LINES = 'sample_lines'
    SAMPLE_UNPARSED = 'sample_unparsed'
    FULL_LINES = 'full_lines'
    FULL_UNPARSED = 'full_unparsed'