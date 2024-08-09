# Haiku Generator Using Markov Chain Analysis

---

### Outstanding Issues (To Be Resolved)

1. ~~**Infinite Loop Bug**: There's a bug where the program can occasionally get stuck in an infinite loop while trying to find the next word. This usually happens when no suitable word is found that fits the remaining syllable count. We'll need to fix that, I guess I could choose a word at random until one works.~~
      ** DONE **

3. ~~**User Interface Improvements**: Need to tidy up the user interface a bit. Feels clunky, especially after regen.~~
      ** DONE **

---

### Project Overview

This project is a Haiku Generator that uses Markov Chain analysis to create haikus from a given text input. The generator builds each line of the haiku based on the traditional 5-7-5 syllable structure. You can even regenerate specific lines if you’re not satisfied with the first result. 

### How It Works

1. **Markov Chain Setup**: The program starts by processing an input text file to create a word map where each word is linked to possible next words. This map helps the program generate each line of the haiku by selecting words that naturally follow each other in the original text.

2. **Syllable Counting**: The generator keeps track of syllables to ensure that the first line has 5 syllables, the second line has 7, and the third line has 5, just like a traditional haiku.

3. **Line Generation**:
   - **First Line**: The program picks a random word to start, then uses the Markov Chain to select the following words until the line reaches 5 syllables.
   - **Second and Third Lines**: It repeats the process for the second and third lines, using the last word from the previous line to maintain a natural flow.

4. **User Interaction**: After the haiku is generated, you're given the option to regenerate the second or third lines if you want to see different variations, or you can exit the program if you're happy with the result.

### Features

- **Unique Haiku Generation**: Every haiku is unique, created based on the input text and random word selection.
- **Line Regeneration**: You can regenerate individual lines to explore different possibilities, adding an element of creativity.
- **Syllable Accuracy**: The program ensures that each line follows the 5-7-5 syllable pattern, true to the haiku tradition.

---

