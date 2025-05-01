// Copyright (C) 2025  CoolCat467
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.

package com.signinapp.signin;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.PasswordField;
import javafx.scene.control.Button;
import java.io.InputStream;

import java.io.File;
import java.net.URL;
import java.net.URISyntaxException;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class HelloController {
    @FXML
    private TextField us;
    @FXML
    private PasswordField ps;
    @FXML
    private Button submit;

    @FXML
    protected void login() {
        String username = us.getText();
        String password = ps.getText();

        // System.out.println(this.get_login_credentials_file());
        DynamicArray<String[]> credentials = read_credentials();
        boolean success = check_credentials(username, password, credentials);
        System.out.printf("success = %b\n", success);
    }

    private boolean check_credentials(String username, String password, Iterable<String[]> credentials){
        for (String[] row : credentials){
            if (row[0].equals(username) && row[1].equals(password)){
                return true;
            }
        }
        return false;
    }

    private File get_login_credentials_file() {
        URL resource = getClass().getResource("/creds.csv");
        // System.out.printf("resource = %s\n", resource);
        if (resource == null){
            System.out.println("resource is null");
            return new File("");
        }
        try {
            return new File(resource.toURI());
        } catch (URISyntaxException exc) {
            System.out.println(exc);
            return new File("");
        }
    }

    private static void print_file(File file){
        System.out.println("Printing file\n");
        try {
            Scanner reader = new Scanner(file);
            while (reader.hasNextLine()){
                System.out.println(reader.nextLine());
            }
            reader.close();
        } catch (FileNotFoundException exc) {
            System.out.println("File not found.");
            System.out.println(exc);
        }
        System.out.println("End of file");
    }

    private DynamicArray<String[]> read_csv(File file, int max_columns) throws FileNotFoundException{
        DynamicArray<String[]> data = new DynamicArray<>(String[].class);

        Scanner reader = new Scanner(file);

        while (reader.hasNextLine()){
            data.append(reader.nextLine().split(",", max_columns));
        }
        reader.close();

        return data;
    }

    private DynamicArray<String[]> read_credentials() {
        File credentials = this.get_login_credentials_file();
        // print_file(credentials);
        try {
            return read_csv(credentials, 2);//.get_raw();
        } catch (FileNotFoundException exc) {
            System.out.println("Credentials file not found.");
            System.out.println(exc);
            // return new String[0][0];
            return new DynamicArray<>(String[].class);
        }
    }

    private static void print_(String[] sequence){
        System.out.print("[");
        for (int i=0; i<sequence.length; i++){
            System.out.printf("\"%s\"", sequence[i]);
            if (i < sequence.length - 1){
                System.out.print(", ");
            }
        }
        System.out.print("]");
    }

    private static void print_(String[][] sequence){
        System.out.print("[");
        for (int i=0; i<sequence.length; i++){
            print_(sequence[i]);
            if (i < sequence.length - 1){
                System.out.print(", ");
            }
        }
        System.out.print("]");
    }

    private static void print(String[][] sequence){
        print_(sequence);
        System.out.println();
    }
    private static void print(String[] sequence){
        print_(sequence);
        System.out.println();
    }
}
