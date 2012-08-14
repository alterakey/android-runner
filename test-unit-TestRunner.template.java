package x.y.z;

import com.xtremelabs.robolectric.Robolectric;
import com.xtremelabs.robolectric.RobolectricTestRunner;
import com.xtremelabs.robolectric.shadows.ShadowSimpleAdapter;
import org.junit.runners.model.InitializationError;

public class TestRunner extends RobolectricTestRunner {
    public TestRunner(Class testClass) throws InitializationError {
        super(testClass);
    }

    @Override
    protected void bindShadowClasses() {
        super.bindShadowClasses();
        Robolectric.bindShadowClass(ShadowSimpleAdapter.class);
    }
}
