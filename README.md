# multisyllabic-rhymer

Find multisyllabic rhymes (perfect, slant, and internal) within the CMU Pronouncing Dictionary.

```
$ python multisyllabic_rhymer.py cigar
No perfect rhymes.

Internal rhymes: cigars, degarmo, disregard, disregarded, disregarding, disregards, regard, regarded...

Slant rhymes: bedard, bellard, benard, bevard, billard, bizarre, bizzaro, bradycardia, cisar, cynara...
```

## Perfect, internal, and slant rhymes

Poets, lyricists, and rappers often go beyond the limited set of perfect rhymes in their work. The scope of possible rhymes is broadened by including slant rhymes (such as guitar and cigar), which do not require matching consonants before the final position. The possibilities expand further by including internal rhymes (such as guitar and departure), which do not require that the matching syllables occur in the final position.

Beyond a single syllable, rhymes become more sonically pleasing and virtuosic when they match (or at least slant) multiple stressed syllables (such as Hacky Sack and Cracker Jack). However, most rhyming tools display only perfect rhymes on the final syllable.

Perfect rhymes are a subset of internal rhymes, which in turn are a subset of slant rhymes. However, the program only displays rhymes in their most specific category.

## How it works

This program extends the rich functionality of the Python library [Pronouncing](https://github.com/aparrish/pronouncingpy) to display perfect, internal, and slant rhymes for a user-inputted word.

First, it converts the given input to a list of phonemes, or units of speech sound. It searches the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) for perfect multisyllabic rhymes, drawing on the input's full syllabic content, not only the final syllable.

To find slant rhymes for these multiple syllables, it uses the vowels but accepts any intermediate consonants, then conducts another (more lenient) search. It then displays all perfect and slant rhymes.
