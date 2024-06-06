import random 

class WordFinder:
   """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
   def __init__(self, path):
        """Read dictionary and reports # items read."""
     
     # open file
        dict_file = open(path)

     # parse words file and save to var
        self.words = self.parse(dict_file)

     # reads through num of words in file
        print(f"{len(self.words)} words read")

   def parse(self, dict_file):
        """Parse dict_file -> list of words."""

     # loops through file and returns each individual line stripped
        return [w.strip() for w in dict_file]

   def random(self):
        """Return random word."""

        return random.choice(self.words)



# SUBCLASS
class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

     # loop through file and strip white spaces
        return [w.strip() for w in dict_file
               #   return if stripped and is not a comment (contains #)
                if w.strip() and not w.startswith("#")]

print(WordFinder.__init__("words.txt"))