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
 * Пример взять из: http://selendroid.io/setup.html
 * */

public class Test1 {

    @Test
    public void test() throws Exception {
        SelendroidCapabilities capa = new SelendroidCapabilities("io.selendroid.testapp:0.10.0");

        WebDriver driver = new SelendroidDriver(capa);
        WebElement inputField = driver.findElement(By.id("my_text_field"));
        Assert.assertEquals("true", inputField.getAttribute("enabled"));
        inputField.sendKeys("Selendroid");
        Assert.assertEquals("Selendroid", inputField.getText());
        driver.quit();
    }

}
