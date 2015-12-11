import java.util.HashMap;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.io.*;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.nio.charset.StandardCharsets;

public class testParser {
    static ArrayList<String> mostFrequentWords;
    static Scanner sc2 = null;
    static Scanner wordScanner = null;
    static Character c = null;
    static String word = null;
    static PrintWriter writer = null;
    static int kFrequentWords = 1000;

    public static void main(String[] args) {
        Scanner commonwords = null;
        try {
            commonwords = new Scanner(new File("commonwords.txt"));
        } catch (FileNotFoundException e) {
            System.out.println("File not found! (weird)");
        }
        mostFrequentWords = new ArrayList<String>();
        for (int i = 0; i < kFrequentWords; i++) {
            mostFrequentWords.add(commonwords.next());
        }
        commonwords.close();
        String directoryPath = "parsedatamore";
        File dir = new File(directoryPath);
        deleteDirectory(dir);
        if (!dir.mkdir()) {
            System.out.println("parsedata directory not created successfully.");
        }
        String[] authors = {"ARISTOTLE", "DICKENS", "DOYLE", "EMERSON", "HAWTHORNE",
        "IRVING", "JEFFERSON", "KANT", "KEATS", "MILTON", "PLATO", "POE", 
        "SHAKESPEARE", "STEVENSON", "TWAIN", "WILDE"};
        for (String author : authors) {
            parseFiles(author);
        }
    }

    public static void deleteDirectory (File dir) {
        File[] files = dir.listFiles();
        for (File file : files) {
            if (file.isDirectory()) {
                deleteDirectory(dir);
            } else {
                file.delete();
            }
        }
        dir.delete();
    }

    /**
     * Parses all files for a given author
     * @param author [description]
     */
    public static void parseFiles(String author) {
        File authorFile = new File("parsedatamore/" + author.toLowerCase() + ".txt");
        try {
            authorFile.createNewFile();
        } catch (IOException e) {
            System.out.println(author + "file could not be created.");
        }
        String directoryPath = "AUTHORS/" + author;
        File dir = new File(directoryPath);
        File[] directoryListing = dir.listFiles();
        if (directoryListing != null) {
            try {
                writer = new PrintWriter(new BufferedWriter(new FileWriter(authorFile, true)));
            } catch (IOException e) {
                System.out.println("Writer could not be created");
                return;
            }
            for (File child : directoryListing) {
                parseArticle2(child);
            } 
            writer.close();
        } else {
            System.out.println("Error: not a directory");
        }
    }

    /**
     * filePath: file to read, by default writes parsed data to authorFile in parseFiles
     * Good stack overflow on regex: http://stackoverflow.com/questions/19600875/count-the-number-of-sentence
     * Post on reading all test from file: http://stackoverflow.com/questions/326390/how-to-create-a-java-string-from-the-contents-of-a-file
     * @param filePath path to file
     */
    public static void parseArticle2(File filePath) {
        /** Stores number of occurences of words and punctuation respepectively */
        HashMap<String, Integer> wordCount = new HashMap<String, Integer>();
        List<String> lines = null;
        try {
            lines = Files.readAllLines(filePath.toPath(), StandardCharsets.UTF_8);
        } catch (IOException e) {
            try {
                lines = Files.readAllLines(filePath.toPath(), StandardCharsets.UTF_16);
            } catch (IOException e2) {
                System.out.println("Error while parsing file");
                System.out.println(filePath);
                e2.printStackTrace();
                return;
            }
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
        // only considering files that are large enough
        if (numwords > 1000) {
            writer.print((double) numwords);
            writer.print(" ");
            writer.print((double) periods);
            writer.print(" ");
            writer.print((double) questionMarks);
            writer.print(" ");
            writer.print((double) exclamationMarks);
            writer.print(" ");
            for (int i = 0; i < kFrequentWords; i++) {
                Integer count = wordCount.get(mostFrequentWords.get(i));
                if (count != null) {
                    writer.print((double) count);    
                } else {
                    writer.print(0.0);
                }
                writer.print(" ");
            }
            writer.println();
        } else {
            return;
        }
        System.out.println(numwords);

    
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