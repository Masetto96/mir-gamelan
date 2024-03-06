
## Introduction and scope
Despite being an essential part of the cultural heritage of one of the most populated countries in the world, the Gamelan tradition remains unexplored from a computational musicological point of view. This is partly due to the lack of datasets and algorithms specially developed for the tradition.
Pitch detection algorithms tend to be biased to western tuning systems, which makes it necessary to test their efficiency when applied to gamelan music. On the other hand, the cultural value of gamelan traditions urge us to review and eventually adapt these algorithms, thus developing the scope of MIR.

## Dataset
The dataset includes recordings from three gamelan ensembles. The first ensemble offers isolated tones from various gamelan instruments along with synthetic arrangements of 10 gamelan pieces using these recordings. Each arrangement includes stems for individual tracks corresponding to each instrument. The second ensemble is not relevant to the project as it focuses on the non-melodic Kendhang instrument. The third ensemble provides one-shot recordings of different gamelan instruments but lacks arrangements, potentially limiting its usefulness for the project.

# Roadmap
1. Separate harmonic from percussive component, this will facilitate the harmonic analysis (very simple librosa) [10-march?]
