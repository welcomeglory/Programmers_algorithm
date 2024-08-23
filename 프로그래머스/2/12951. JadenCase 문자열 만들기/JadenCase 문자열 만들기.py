def solution(s):
    words = s.split(" ")
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
#     s = s.lower()
#     s_listed = list(s)
#     if s_listed[0].isalpha():
#         s_listed[0] = s_listed[0].upper()

#     for i in range(1,len(s_listed)):
#         if s_listed[i] == " ":
#             s_listed[i+1] = s_listed[i+1].upper()
            
#     return "".join(s_listed)
    
