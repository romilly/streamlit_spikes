Decompose the “Content” into clear and simple propositions, ensuring they are interpretable out of context.
1. Split compound sentence into simple sentences. Maintain the original phrasing from the input whenever possible. 
2. For any named entity that is accompanied by additional descriptive information, separate this information into its own distinct proposition.
3. Decontextualize the proposition by adding necessary modifier to nouns or entire sentences and replacing pronouns (e.g., “it”, “he”, “she”, “they”, “this”, “that”) with the full name of the entities they refer to.
4. Present the results as a list of strings, formatted in JSON.

Content:

The pericardium (pl.: pericardia), also called pericardial sac, is a double-walled sac containing the heart and the roots of the great vessels.

It has two layers, an outer layer made of strong inelastic connective tissue (fibrous pericardium), and an inner layer made of serous membrane (serous pericardium). It encloses the pericardial cavity, which contains pericardial fluid, and defines the middle mediastinum. It separates the heart from interference of other structures, protects it against infection and blunt trauma, and lubricates the heart's movements.

![propostionizer.png](..%2F..%2F..%2F..%2FPictures%2Fpropostionizer.png)