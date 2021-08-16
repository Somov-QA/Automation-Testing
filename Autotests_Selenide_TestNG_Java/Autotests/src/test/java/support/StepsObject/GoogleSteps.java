package support.StepsObject;

import com.codeborne.selenide.SelenideElement;
import java.util.List;
import support.PageObjects.GooglePage;

public class GoogleSteps {
    public void searchValue(String value) {
        SelenideElement inputElement = GooglePage.getInputSearch();
        inputElement.setValue(value).pressEnter();
    }

    public int getCountResultSearch() {
        List<SelenideElement> list = GooglePage.getListResultsSearch();
        return list.size();
    }
}
