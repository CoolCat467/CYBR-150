package com.signinapp.signin;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.geometry.Rectangle2D;
import javafx.stage.Screen;

import java.io.IOException;

public class HelloApplication extends Application {
    public final double width = getScreenDimensions()[0] / 3;
    public final double height = getScreenDimensions()[1] / 3;

    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(this.getClass().getResource("hello-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), width, height);
        String css = this.getClass().getResource("/CSS/styles.css").toExternalForm();
        // System.out.printf("css = %s\n", css);
        scene.getStylesheets().add(css);
        stage.setTitle("Sign In");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch();
    }

    public static double[] getScreenDimensions(){
        Rectangle2D screen_bounds = Screen.getPrimary().getBounds();
        double[] dim = new double[2];
        dim[0] = screen_bounds.getWidth();
        dim[1] = screen_bounds.getHeight();
        return dim;
    }
}
