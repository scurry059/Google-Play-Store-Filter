/*

Google Play Store Data Filter
Authored by Matthew Steuerer, Nikhil Sankepalli, and Seth Curry
October 7th, 2020
Demonstrates the use of Lists is Python with 2018 Google Play Store Data
Data Source URL: https://www.kaggle.com/lava18/google-play-store-apps

Initial Ideas: create a list of objects where each entry in the list is an app object
Each app will have attributes that correspond to column titles
The user needs to be able to filter on up to three of these attributes
Need to confirm if user should be able to apply multiple filters (ex: category type and content rating)
User inputs their criteria and the program needs to find all records that match
Minimum Requirements: Be able to run the program once and return result, user may have to rerun for additional queries
Ideal Requirements: Be able to have program run in a loop and filter on multiple criteria
Shoot for the Stars Requirements: GUI with program logic

// Reads CSV File
package Comp228;

import java.io.*;
import java.util.Scanner;
public class Info {
    public static void main(String[] args) throws Exception  
    {  
    //parsing a CSV file into Scanner class constructor  
        Scanner sc = new Scanner(new File("C:/Users/drywi/csv/googleplaystore.csv"));  
        sc.useDelimiter(",");   //sets the delimiter pattern  
            while (sc.hasNext())  //returns a boolean value  
    {  
        System.out.print(sc.next());  //find and returns the next complete token from this scanner  
    }   
            sc.close();  //closes the scanner  
        }  
    }  


// Representing Each Object
package Comp228;
import java.util.ArrayList;
import java.util.List;

public class Objects {
    public static void main(String[] args) {
        List<String> object = new ArrayList<>();
        object.add("app");
        object.add("category");
        object.add("rating");
        object.add("reviews");
        object.add("size");
        object.add("installs");
        object.add("type");
        object.add("price");
        object.add("contentRating");
        object.add("genres");
        object.add("lastUpdated");
        object.add("currentVer");
        object.add("androidVer");
        for (String objects : object) {
            
            System.out.printf("%s ", object);
        }
        
        System.out.println();
    }
}

