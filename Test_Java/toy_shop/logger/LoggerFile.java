package Test_Java.toy_shop.logger;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class LoggerFile implements Logger {

    private String fileName;

    public LoggerFile(String fileName) {
        this.fileName = fileName;
    }

    @Override
    public void log(String message) {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(fileName, true))) {
            writer.write(message + "\n");
        } catch (IOException e) {
            System.err.println("Something wrong " + e.getMessage());
            throw new UnsupportedOperationException("Unimplemented method 'log'");
        }
        
    }
    
}
