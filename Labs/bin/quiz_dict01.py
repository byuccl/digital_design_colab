def quiz_func(key):
  dictionary = {"01": ["What is this question?", "Answer", "This is a hint"],
                "02": ["What is A AND B, if A=1 and B=0?", "0", "Check the Truth Table"],
                "03": ["What is: (A AND B) AND A, if A=1 and B =0", "0", "The parenthesis happen first"],
                "04": ["What is A or B if A=1 B=0?", "1", "Check the Truth Table"],
                "05": ["What is (A or B) or A if A=0 and B=1?", "1", "The parenthesis happen first"],
                "06": ["What is NOT 1?", "0", ""],
                "07": ["What is (NOT (A OR B) ) or A if A = 0 and B =1?", "0", "" ],
                "08": ["What is A XOR B if A = 1 and B =1?", "0", "Check the Truth Table"],
                "09": ["What is (A XOR B) XOR A if A=0 and B = 1?", "1", ""],
                "10": ["What is the output of 4’b1001&4’b1011?", "1001", "The answer will be 4 digits, 1's or 0's"],
                "11": ["What is the output of 4’b1001|4’b1011?", "1011",  "The answer will be 4 digits, 1's or 0's"],
                "12": ["What is the output of 4’b1001^4b’1011?", "0010", "The answer will be 4 digits, 1's or 0's"],
                "13": ["What is the output of 4’b1001&&4’b1011?", "1", "The answer will be a single digit, 1 or 0"],
                "14": ["What is the output of 4’b1001||4’b1011?", "1", "The answer will be a single digit, 1 or 0"],
                "15": ["What is the output of 4’b1001^^4b’1011?", "0", "The answer will be a single digit, 1 or 0"],
                "16": ["What is the output of &4’b1011`?", "0", "The answer will be a single digit, 1 or 0"],
                "17": ["What is the output of |4’b1011`?", "1", "The answer will be a single digit, 1 or 0"],
                "18": ["What is the output of ^4b’1011`?", "1", ""],
                "19": [f"What is the value of x? \nassign x = 1’b1; \nassign y = 1’b0; \nassign x = y; \n\nA 1’b1 \nB. 1’b0 \nC. An Error will be thrown", "D", "Remember, everything is executed simulatenously"],
                "20": [f"What is the value of x? \nassign x = y;\nassign y = b & 2’b10;\nassign b = 2’b11;\n\nA. 1’b1 \nB. 1’b0 \nC. 2’b11 \nD. 2’b10 \nE. An Error will be thrown", "D", ""],
                "21": [f"What is the value of x?\nalways_comb begin\nx = y;\ny = &&4’b1111;\nend\nA. 1’b1 \nB. 1’b0 \nC. 1’b1111 \nD. An Error will be thrown", "D", ""],
                "22": [f"Which is correct?\nA.logic input [3:0] x \nB. logic [3:0] input x \nC. input logic x [3:0] \nD. input logic [3:0] x \nE. logic input x [3:0]\n", "D", ""],
                "23": [f"What is the value of x? \n(y is in input with the value of 2'b10)\nalways_comb begin\nif(y==0) x = 1;\nelse if(y==1) x = 4; \nelse if(y==2) x = 7; \nelse if (y==3) x = 9; \nelse x = 0\nend\nA. 0 \nB. 4'b0001 \nC. 4'b0011 \nD. 4'b0111 \nE. 4'b1001 \nF. An Error will be thrown\n", "D", ""]

                }
  question = dictionary[key][0]
  answer = dictionary[key][1]
  hint = dictionary[key][2]
  response = input(question + "  ")
  if response.isalpha():
    response = response.upper()
  if response == answer:
    print(f"\nCorrect")
  else:
    print(f"\n%s\nIncorrect" % hint)
# quiz_func("23")
