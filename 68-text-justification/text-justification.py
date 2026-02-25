class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        
        while i < len(words):
            line_length = len(words[i])
            last = i + 1
            
            while last < len(words):
                if line_length + 1 + len(words[last]) > maxWidth:
                    break
                line_length += 1 + len(words[last])
                last += 1
            
            line = ""
            number_of_words = last - i
            
            if last == len(words) or number_of_words == 1:
                for j in range(i, last):
                    line += words[j] + " "
                
                line = line.strip()
                line += " " * (maxWidth - len(line))
            
            else:
                total_word_length = sum(len(words[j]) for j in range(i, last))
                total_spaces = maxWidth - total_word_length
                gaps = number_of_words - 1
                
                space_between = total_spaces // gaps
                extra_spaces = total_spaces % gaps
                
                for j in range(i, last - 1):
                    line += words[j]
                    line += " " * (space_between + (1 if j - i < extra_spaces else 0))
                
                line += words[last - 1]
            
            result.append(line)
            i = last
        
        return result