# Retrieval Augmented Generation System

In this (work-in-progress) project, I create a rag from first principles (reasoning from the ground up with no internet tutorials) in python.
The project intuitively is quite straightforward:
1. create a system to chunk the text
2. Create a VectorDB to store these chunks and retrieve them.
3. Use an existing embedding model like Bert (eventually replace with a custom-trained model).
4. Re-rank the retrieved chunks using a reranker model
5. Pass the re-ranked chunks through to an LLM like OpenAI gpt4

Note: I've put this project on hold to work on some more urgent projects, have a look at these recent finished projects instead:
- [BlogEditor](https://github.com/AnirudhhRamesh/BlogEditor): Auto-transcribe & generate blog assets (thumbnails, Substack content, social captions) from a 2-person zoom recording, photo & resume.
- [Ambitious x Driven](http://www.ambitiousxdriven.com) (using BlogEditor^) which has 1.3K readers and I'm monetizing via job boards + sponsors (and handling lead generation & sales calls + closing)
- Efficient 3D Gaussian Splatting (research at the Scalable Parallel Computing Lab, advised by Prof. Torsten Hoefler, @ETH Zurich)
