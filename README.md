# multisyllabic-rhymer

Find multisyllabic rhymes (perfect, internal, and slant) within the CMU Pronouncing Dictionary.

```
$ pip install -r requirements.txt
$ python multisyllabic_rhymer.py cigar
No perfect rhymes.

Internal rhymes: cigars, degarmo, disregard, disregarded, disregarding, disregards, regard, regarded...

Slant rhymes: bedard, bellard, benard, bevard, billard, bizarre, bizzaro, bradycardia, cisar, cynara...
```

## Perfect, internal, and slant rhymes

Poets, lyricists, and rappers often go beyond the limited set of perfect, one-syllable rhymes in their work. Rhymes become more sonically pleasing and virtuosic when they match (or at least slant) multiple stressed syllables (such as Hacky Sack and Cracker Jack). However, most rhyming tools display only perfect rhymes on the final syllable.

Beyond perfect rhymes, the scope of possibility is broadened by including internal rhymes (such as cigar and disregarded), which rhyme perfectly but not on the final syllable. The possibilities expand further by including slant rhymes (such as cigar and bizarre), which match vowel sounds and final consonants, but do not require matching consonants before the final syllable. Perfect rhymes are a subset of internal rhymes, which in turn are a subset of slant rhymes, and each candidate is only displayed in the most descriptive category it satisfies.

## How it works

This program extends the rich functionality of the Python library [Pronouncing](https://github.com/aparrish/pronouncingpy) to display perfect, internal, and slant rhymes for a user-inputted word.

First, it converts the given input to a list of phonemes, or units of speech sound. It searches the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) for perfect rhymes, drawing on the input's full syllabic content, not only the final syllable, but requiring that there be no syllables after the rhyming part.

To find internal rhymes, it repeats a search for the same rhyming part, but allows for syllables afterwards. To display only internal rhymes, it subtracts the set of perfect rhymes from the list of internal rhymes.

To find slant rhymes for these multiple syllables, it uses the vowels and final consonant, but accepts any intermediate consonants, then conducts a final, more lenient search. It subtracts the sets of perfect and internal rhymes from this list, then displays all three categories of multisyllabic rhymes.

## Further directions

Since the rhyme matching operates entirely on phonemes, it would be possible to input and output phrases of multiple words.

To fine-tune the search for slant rhymes, intermediate consonants could require a level of phonetic similarity, such as 'S' with 'SH', 'F', or 'TH'. 

Pronouncing lists syllabic stress information, which could be used to generate lyrics conforming to a desired stress pattern.
