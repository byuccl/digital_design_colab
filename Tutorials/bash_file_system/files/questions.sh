
questions=("QuestionOne" "QuestionTwo" "QuestionThree" "QuestionFour" "QuestionFive" "QuestionSix" "QuestionSeven")
rm -rf /content/Questions
mkdir /content/Questions
cd /content/Questions

for question in "${questions[@]}"; do
    mkdir $question
done

#Question One
files=("one.txt" "two.txt" "three.txt" "um.sv" "file.file" "bash.bash")

for file in "${files[@]}"; do   
    touch /content/Questions/QuestionOne/"$file";
done

#Question 4
echo "This is a text file. There are words in it" > /content/Questions/QuestionFour/text.txt
#Question 5
echo "This is a different text file. There are more words in it" > /content/Questions/QuestionFive/text.txt
#Question 7
echo "This is a totally different text file. There are a bunch more words in it" > /content/Questions/QuestionSeven/text.txt
