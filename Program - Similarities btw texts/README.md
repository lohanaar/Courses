## Introduction
Manuel Estandarte is a monitor in the Introduction to Textual Production I course at the University of Pasárgada (UPA). During the school term, Manuel discovered that a COH-PIAH epidemic was spreading throughout the UPA. This rare and highly contagious disease causes infected individuals to involuntarily produce texts very similar to those of other people. After submitting the first essay, Manuel suspected that some students were suffering from COH-PIAH. Manuel, concerned about the health of the class, decided to look for a method to identify cases of COH-PIAH. To do this, he uses this program to help him identify infected students.
## Authorship detection
Different people have different writing styles; for example, some people prefer shorter sentences, others prefer longer sentences. Using various text statistics, it is possible to identify aspects that function as a “signature” of its author and, therefore, it is possible to detect whether two given texts were written by the same person. In other words, this “signature” can be used to detect plagiarism, forensic evidence or, in this case, to diagnose the serious disease COH-PIAH.
## Linguistic traits
In this program, the following statistics are used to detect the disease:
-	Average word length: Simple average of the number of characters per word.
-	Type-Token Ratio: Number of different words used in a text divided by the total number of words.
-	Hapax Legomana Ratio: Number of words used once divided by the total number of words.
-	Average sentence length: Simple average of the number of characters per sentence.
-	Sentence complexity: Simple average of the number of phrases per sentence.
-	Average phrase length: Simple average of the number of characters per phrase.
## Program operation
The linguistic features that this program uses are calculated as follows:
- **Average word length** is the sum of word lengths divided by the total number of words.
- **Type-Token Ratio** is the number of different words divided by the total number of words. For example, in the sentence "The cat hunted the mouse", we have 5 words in total (the, cat, hunted, the, mouse) but only 4 different ones (the, cat, hunted, mouse). In this sentence, the Type-Token relationship is worth 4/5 = 0.8 
- **Hapax Legomana ratio** is the number of words that appear once divided by the total number of words. For example, in the sentence "The cat hunted the mouse", we have 5 words in total (the, cat, hunted, the, mouse) but only 3 that appear only once (cat, hunted, mouse). In this sentence, the Hapax Legomana relationship is worth 3/5 = 0.6
- **Average sentence length** is the sum of the number of characters in all sentences divided by the number of sentences (characters that separate one sentence from another should not be counted as part of the sentence).
- **Sentence complexity** is the total number of phrases divided by the number of sentences.
- **Average phrase length** is the sum of the number of characters in each phrase divided by the number of phrase in the text (characters that separate one phrase from another should not be counted as part of the phrase).

*Note: Sentences are separated by (.!?),  and phrases are separated  by (,:;).*

After calculating these values for each text, the CO-PIAH program compares them with the signature's text provided for those infected with COH-PIAH. The degree of similarity between two texts, a e b, is given by the formula:

![image](https://github.com/lohanaar/Courses/assets/122733477/1d69aceb-a953-4caf-8097-4be243d1dc71)

Where:
-	***S ab***    is the degree of similarity between texts a e b;
-	***f i,a***   is the value of each linguistic feature i not text a; 
-	***f i,b***   is the value of each linguistic feature i not text b.
##
To test, use the texts below:

**Original Text:**

"If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough."

**CO-PIAH Case - Test_Text_1:**

"When observing your life, focus on the positives, and abundance will grow. Dwelling on life's lacks leads to perpetual insufficiency."

**Test_Text_2:**

"In the realm of quantum physics, particles dance unpredictably, defying classical notions of causality. Probability waves govern the behavior of these elusive entities, introducing a realm of uncertainty to the fundamental fabric of reality."

**Test_Text_3:**

"The vibrant sunset painted the sky with hues of orange and pink, casting a warm glow over the serene landscape. Birds soared gracefully, embracing the freedom of the open air."
