module com.signinapp.signin {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.bootstrapfx.core;
    requires com.almasb.fxgl.all;

    opens com.signinapp.signin to javafx.fxml;
    exports com.signinapp.signin;
}
