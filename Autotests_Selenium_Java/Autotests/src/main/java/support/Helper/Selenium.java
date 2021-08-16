package support.Helper;

import org.openqa.selenium.*;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.remote.CapabilityType;
import org.openqa.selenium.remote.DesiredCapabilities;

public class Selenium {
    public static WebDriver driver;

    public static String getDriverPath() {
        String path = System.getProperty("user.dir") + "\\driver\\chromedriver.exe";
        System.out.println("WebDriver: path ["+path+"]");
        return path;
    }

    public static void initWebDriver() {
        System.setProperty("webdriver.chrome.driver", getDriverPath());
        driver = new ChromeDriver();
        System.out.println("WebDriver: init");
    }

    public static void browserFullScreen() {
        driver.manage().window().maximize();
        System.out.println("Browser: full screen");
    }

    public static void quitWebDriver() {
        driver.close();
        driver.quit();
        System.out.println("WebDriver: quit");
    }
}

