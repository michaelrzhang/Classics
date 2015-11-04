import java.util.*;
import java.io.*;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.nio.charset.StandardCharsets;

public class testParser {
    static Scanner sc2 = null;
    static Scanner wordScanner = null;
    static Character c = null;
    static String word = null;
    static PrintWriter writer = null;

    public static void main(String[] args) {
        parseFiles("EMERSON");
    }

    public static void parseFiles(String author) {
        String directoryPath = "AUTHORS/" + author;
        File dir = new File(directoryPath);
        File[] directoryListing = dir.listFiles();
        int file = 0;
        File directory = new File(author.toLowerCase());
        if (!directory.mkdir()) {
            System.out.println("Directory not created successfully");
        }
        if (directoryListing != null) {
            for (File child : directoryListing) {
                file += 1;
                parseArticle2(child, author.toLowerCase(), file);
            } 
        } else {
            System.out.println("Error: not a directory");
        }
    }

    /**
     * Good stack overflow on regex: http://stackoverflow.com/questions/19600875/count-the-number-of-sentence
     * Post on reading all test from file: http://stackoverflow.com/questions/326390/how-to-create-a-java-string-from-the-contents-of-a-file
     * @param filePath path to file
     */
    public static void parseArticle2(File filePath, String author, int numfile) {
        /** Stores number of occurences of words and punctuation respepectively */
        HashMap<String, Integer> wordCount = new HashMap<String, Integer>();
        List<String> lines = null;
        try {
            lines = Files.readAllLines(filePath.toPath(), StandardCharsets.UTF_8);
        } catch (IOException e) {
            System.out.println("Error while parsing file");
            return;
        }
        int periods, questionMarks, exclamationMarks, numwords;
        periods = questionMarks = exclamationMarks = numwords = 0;
        /** parses with regex, wordCount keeps track of words and count of words */
        for (String line : lines) {
            String[] words = line.replaceAll("[^a-zA-Z ]", "").toLowerCase().split("\\s+");
            numwords += words.length;
            for (String word : words) {
                if (!wordCount.containsKey(word)) {
                    wordCount.put(word, 0);
                }
                wordCount.put(word, wordCount.get(word) + 1);
            }
            periods += line.length() - line.replace(".", "").length();
            questionMarks += line.length() - line.replace("!", "").length();
            exclamationMarks += line.length() - line.replace("?", "").length();
        }
        File newFile = new File(author + "/" + String.valueOf(numfile) + ".txt");
        try {
            writer = new PrintWriter(newFile);
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        System.out.println(numwords);
        writer.println(numwords);
        writer.println(periods);
        writer.println(questionMarks);
        writer.println(exclamationMarks);
        writer.close();
        /** Debugging */
        // for (String s : wordCount.keySet()) {
        //     System.out.println(s);
        //     System.out.println(wordCount.get(s));
        //     System.out.println();
        // }
    }

    /**
     * parseArticle2 is better
     * Given a file path, output relevant information regarding the file
     * @param filePath path to file
     */
    public static void parseArticle(String filePath) {
        /** Stores number of occurences of words and punctuation respepectively */
        HashMap<String, Integer> words = new HashMap<String, Integer>();
        HashMap<Character, Integer> punctuation = new HashMap<Character, Integer>();
        try {
            sc2 = new Scanner(new File(filePath));
        } catch (FileNotFoundException e) {
            e.printStackTrace();  
        }
        while (sc2.hasNextLine()) {                
            String nextLine = sc2.nextLine();
            wordScanner = new Scanner(nextLine);
            while (wordScanner.hasNext()) {
                word = wordScanner.next();
                if (!Character.isLetter(word.charAt(0))) {
                    c = word.charAt(0);
                    if (!punctuation.containsKey(c)) {
                        punctuation.put(c, 0);
                    }
                    punctuation.put(c, punctuation.get(c) + 1);
                    word = word.substring(1, word.length());
                }
                if (word.length() >= 1 && !Character.isLetter(word.charAt(word.length() - 1))) { // may want to save word.length() to variable
                    c = word.charAt(word.length() - 1);
                    if (!punctuation.containsKey(c)) {
                        punctuation.put(c, 0);
                    }
                    punctuation.put(c, punctuation.get(c) + 1);
                    word = word.substring(0, word.length() - 1);
                }
            }
            if (!words.containsKey(word)) {
                words.put(word, 0);
            }
            words.put(word, words.get(word) + 1);  // industry standard
        }

    }
    
}