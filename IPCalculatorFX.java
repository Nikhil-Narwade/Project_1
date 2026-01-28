import javafx.scene.control.Label;

import javafx.application.Application;
import javafx.geometry.*;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.stage.Stage;

public class IPCalculatorFX extends Application {

    TextField ipField = new TextField();
    TextField maskField = new TextField("255.255.255.0");
    TextField classField = new TextField();
    TextField typeField = new TextField();
    TextField hostField = new TextField();
    TextField binIpField = new TextField();
    TextField binMaskField = new TextField();
    TextField binNetField = new TextField();
    TextField networkField = new TextField();
    TextField broadcastField = new TextField();

    @Override
    public void start(Stage stage) {

        VBox root = new VBox(20);
        root.setPadding(new Insets(20));
        root.getStyleClass().add("root");

        Label title = new Label("IP Calculator");
        title.getStyleClass().add("title");

        HBox topRow = new HBox(20,
                ipInfoCard(),
                networkInfoCard()
        );

        HBox bottomRow = new HBox(20,
                binaryCard(),
                subnetCard()
        );

        root.getChildren().addAll(title, topRow, bottomRow);

        Scene scene = new Scene(root, 900, 550);
        scene.getStylesheets().add("style.css");

        stage.setTitle("IP Calculator");
        stage.setScene(scene);
        stage.setResizable(false);
        stage.show();
    }

    // ---------------- CARDS ----------------

    VBox ipInfoCard() {
        VBox box = card("IP Information");

        ipField.setPromptText("e.g. 10.70.6.1");

        Button compute = new Button("Compute");
        compute.setOnAction(e -> compute());

        box.getChildren().addAll(
                labeled("IP Address", ipField),
                labeled("Subnet Mask", maskField),
                compute
        );
        return box;
    }

    VBox networkInfoCard() {
        VBox box = card("Network Information");

        classField.setEditable(false);
        typeField.setEditable(false);

        box.getChildren().addAll(
                labeled("IP Class", classField),
                labeled("Address Type", typeField),
                labeled("Hosts", hostField)
        );
        return box;
    }

    VBox binaryCard() {
        VBox box = card("Binary Information");

        binIpField.setEditable(false);
        binMaskField.setEditable(false);
        binNetField.setEditable(false);

        box.getChildren().addAll(
                labeled("Binary IP", binIpField),
                labeled("Binary Mask", binMaskField),
                labeled("Binary Network", binNetField)
        );
        return box;
    }

    VBox subnetCard() {
        VBox box = card("Subnet Information");

        networkField.setEditable(false);
        broadcastField.setEditable(false);

        box.getChildren().addAll(
                labeled("Network ID", networkField),
                labeled("Broadcast ID", broadcastField)
        );
        return box;
    }

    // ---------------- LOGIC ----------------

    void compute() {
        try {
            int[] ip = parse(ipField.getText());
            int[] mask = parse(maskField.getText());

            int[] net = new int[4];
            int[] broad = new int[4];

            for (int i = 0; i < 4; i++) {
                net[i] = ip[i] & mask[i];
                broad[i] = net[i] | (~mask[i] & 255);
            }

            classField.setText(ipClass(ip[0]));
            typeField.setText(isPrivate(ip) ? "Private" : "Public");

            int hosts = (int) Math.pow(2, 32 - maskBits(mask)) - 2;
            hostField.setText(String.valueOf(hosts));

            binIpField.setText(toBinary(ip));
            binMaskField.setText(toBinary(mask));
            binNetField.setText(toBinary(net));

            networkField.setText(toDot(net));
            broadcastField.setText(toDot(broad));

        } catch (Exception e) {
            alert("Invalid IP Address");
        }
    }

    // ---------------- HELPERS ----------------

    VBox card(String title) {
        VBox box = new VBox(12);
        box.getStyleClass().add("card");

        Label t = new Label(title);
        t.getStyleClass().add("card-title");

        box.getChildren().add(t);
        return box;
    }

    HBox labeled(String text, TextField field) {
        VBox v = new VBox(5, new Label(text), field);
        return new HBox(v);
    }

    int[] parse(String s) {
    String[] p = s.split("\\.");
    if (p.length != 4) throw new IllegalArgumentException();

    int[] a = new int[4];
    for (int i = 0; i < 4; i++) {
        int val = Integer.parseInt(p[i]);
        if (val < 0 || val > 255)
            throw new IllegalArgumentException();
        a[i] = val;
    }
    return a;
}

    String toBinary(int[] a) {
        StringBuilder sb = new StringBuilder();
        for (int i : a)
            sb.append(String.format("%8s", Integer.toBinaryString(i))
                    .replace(' ', '0')).append(".");
        return sb.substring(0, sb.length() - 1);
    }

    String toDot(int[] a) {
        return a[0] + "." + a[1] + "." + a[2] + "." + a[3];
    }

    int maskBits(int[] m) {
        int c = 0;
        for (int i : m) c += Integer.bitCount(i);
        return c;
    }

    String ipClass(int f) {
        if (f <= 127) return "Class A";
        if (f <= 191) return "Class B";
        if (f <= 223) return "Class C";
        return "Class D/E";
    }

    boolean isPrivate(int[] ip) {
        return ip[0] == 10 ||
               (ip[0] == 172 && ip[1] >= 16 && ip[1] <= 31) ||
               (ip[0] == 192 && ip[1] == 168);
    }

    void alert(String msg) {
        Alert a = new Alert(Alert.AlertType.ERROR, msg);
        a.show();
    }

    public static void main(String[] args) {
        launch();
    }
}
