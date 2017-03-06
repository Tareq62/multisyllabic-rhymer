import pronouncing
import string
import copy
import sys


CONSONANTS = set(string.ascii_uppercase)-set('AEIOU')


def get_phones(word):
    """
    Given a user-inputted word, return phones, its corresponding list of phonemes.

    For example, the input guitar yields the list ['G', 'IH0', 'T', 'AA1', 'R']
    """
    phones_for_word = pronouncing.phones_for_word(word)

    if not phones_for_word:
        return None

    phones = phones_for_word[0].split()
    return phones


def _get_vowel_index(phones):
    """
    In preparation to search for slant rhymes, return the position of the first vowel in phones.
    """
    for index, phone in enumerate(phones):
        if phone[0] in 'AEIOU':
            return index


def _get_consonant_indices(phones):
    """
    In preparation to search for slant rhymes, return the positions of all intermediate consonants after the first vowel in phones.
    """
    indices = []

    for index, phone in enumerate(phones):
        if phone[0] in CONSONANTS and index < len(phones) - 1:
            indices.append(index)

    return indices


def _get_rhyming_tail(phones):
    """
    In preparation to search for multisyllabic rhymes, remove characters before the first vowel in phones.

    For example, phones changes from ['G', 'IH0', 'T', 'AA1', 'R'] to ['IH0', 'T', 'AA1', 'R']
    """
    index = _get_vowel_index(phones)
    return phones[index:]


def _slant_rhyme_consonants(phones):
    """
    Replaces intermediate consonants with a period, the wildcard character. The final consonant is preserved.

    For example, replace the intermediate 'T' in ['IH0', 'T', 'AA1', 'R'], leaving ['IH0', '.', 'AA1', 'R']
    """
    consonant_indices = _get_consonant_indices(phones)
    new_phones = copy.copy(phones)

    for index in consonant_indices:
        new_phones[index] = '.'

    return new_phones


def get_perfect_rhymes(phones):
    """
    Given phones, search for perfect, multisyllabic rhymes with no syllables afterwards.
    """
    rhyming_tail = " ".join(_get_rhyming_tail(phones))
    return pronouncing.search(rhyming_tail + "$")


def get_internal_rhymes(phones):
    """
    Given phones, search for internal, multisyllabic rhymes.
    """
    rhyming_tail = " ".join(_get_rhyming_tail(phones))
    return pronouncing.search(rhyming_tail)


def get_slant_rhymes(phones):
    """
    Given phones, return all slant and internal rhymes.

    Slant rhymes do not require matching consonants before the final position. For example, guitar and cigar.
    Internal rhymes do not require the matching syllables to be final. For example, guitar and departure.
    """
    tail = _get_rhyming_tail(phones)
    search = ' '.join(_slant_rhyme_consonants(tail))
    return pronouncing.search(search)


def main(word):
    """
    Search for slant rhymes given word, an argument from the command line.

    For an inputted word not recognized in the CMU dictionary, prompt user to try another word.
    """
    phones = get_phones(word)

    if phones is None:
        print('That word is not recognized. Please check the spelling and avoid proper nouns.')
        exit(1)

    perfect_rhymes = get_perfect_rhymes(phones)
    internal_rhymes = get_internal_rhymes(phones)
    slant_rhymes = get_slant_rhymes(phones)

    perfects_without_word = set(perfect_rhymes) - {word}
    internals_without_perfects = set(internal_rhymes) - set(perfect_rhymes) - {word}
    imperfect_slants = set(slant_rhymes) - set(internal_rhymes) - {word}

    if perfects_without_word:
        print('Perfect rhymes:', ", ".join(sorted(perfects_without_word)), '\n')
    else:
        print('No perfect rhymes.\n')

    if internals_without_perfects:
        print('Internal rhymes:', ", ".join(sorted(internals_without_perfects)), '\n')
    else:
        print('No internal rhymes.\n')

    if imperfect_slants:
        print('Slant rhymes:', ", ".join(sorted(imperfect_slants)))
    else:
        print('No slant rhymes.')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: multisyllabic_rhymer.py word, where word is the rhyme target.')
        exit(1)

    main(sys.argv[1])
