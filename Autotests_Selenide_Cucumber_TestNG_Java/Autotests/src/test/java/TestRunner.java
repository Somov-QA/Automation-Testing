import io.cucumber.testng.AbstractTestNGCucumberTests;
import io.cucumber.testng.CucumberOptions;

@CucumberOptions
(
        features = "features/TestGoogleSearch.feature",
        glue = "support/StepsObject"
)
public class TestRunner extends AbstractTestNGCucumberTests {

}
