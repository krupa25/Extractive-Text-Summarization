from gensim.summarization import summarize
class Abstractive:
    def summarize(request,article):
        summary = summarize(article,word_count=70)
        return summary