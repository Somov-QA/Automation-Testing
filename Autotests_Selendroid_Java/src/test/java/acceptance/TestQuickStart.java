package acceptance;

import io.selendroid.client.SelendroidDriver;
import io.selendroid.common.SelendroidCapabilities;
import io.selendroid.standalone.SelendroidConfiguration;
import io.selendroid.standalone.SelendroidLauncher;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.testng.Assert;
import org.testng.annotations.AfterTest;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;

/*
 * Пример взять из: http://selendroid.io/quickStart.html
 * */

public class TestQuickStart {

    private static WebDriver driver = null;

    @BeforeTest
    public static void setUp() throws Exception {
        SelendroidConfiguration config = new SelendroidConfiguration();
        config.addSupportedApp("apk/calc.apk");
        SelendroidLauncher selendroidServer = new SelendroidLauncher(config);
        selendroidServer.launchSelendroid();

        SelendroidCapabilities caps = new SelendroidCapabilities("com.jee.calc");
        driver = new SelendroidDriver(caps);
    }

    @Test
    public void test() {
        WebElement inputField = driver.findElement(By.id("my_text_field")); //enter a text into the text field
        inputField.sendKeys("Selendroid"); //check if the text has been entered into the text field
        Assert.assertEquals("Selendroid", inputField.getText());
    }

    @AfterTest
    public static void tearDown() {
        driver.close();
    }
}
