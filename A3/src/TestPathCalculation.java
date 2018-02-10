import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

/**
 * @author Meet Patel, patelm16
 *
 */
public class TestPathCalculation {

	PathT path1 = new PathT();
	PathT path2 = new PathT();
	PathT path3 = new PathT();
	PathT path4 = new PathT();
	
	/**
	 * @throws java.lang.Exception
	 */
	@Before
	public void setUp() throws Exception {
		
		path1.add(0, new PointT(0,0));
		path1.add(1, new PointT(5,0));
		path1.add(2, new PointT(5,80));
		path1.add(3, new PointT(180,80));
		path1.add(4, new PointT(180,160));
		
		path2.add(0, new PointT(10,10));
		path2.add(0, new PointT(10,10));
		
		path3.add(0, new PointT(0,0));
		path3.add(1, new PointT(5,0));
		path3.add(2, new PointT(50,0));
		path3.add(3, new PointT(100,10));
		
		path4.add(0, new PointT(0,0));
		path4.add(1, new PointT(0,0));
		path4.add(2, new PointT(180,0));
		path4.add(3, new PointT(180,10));

	}

	/**
	 * @throws java.lang.Exception
	 */
	@After
	public void tearDown() throws Exception {
		
	}
	
	/**
	 * tests totalDistance method
	 * @throws InvalidPositionException 
	 */
	@Test
	public void testTotalDistancePathCalculation() throws InvalidPositionException{
		assertTrue(PathCalculation.totalDistance(path1) == 340); //complex path
		assertTrue(PathCalculation.totalDistance(path2) == 0); //zero length path
		assertTrue(PathCalculation.totalDistance(path4) == 190); //path with 2 coincident points
	}
	
	/**
	 * tests totalTurns method
	 * @throws InvalidPositionException 
	 */
	@Test
	public void testTotalTurnsPathCalculation() throws InvalidPositionException{
		assertTrue(PathCalculation.totalTurns(path1) == 3); //counterclockwise and clockwise turns
		assertTrue(PathCalculation.totalTurns(path3) == 1); //2 collinear segments
	}
	
	
	/**
	 * tests estimatedTime method
	 * @throws InvalidPositionException 
	 */
	@Test
	public void testEstimatedTimePathCalculation() throws InvalidPositionException{
		assertTrue(PathCalculation.estimatedTime(path1) == 22.823746299346155);//complex path
		assertTrue(PathCalculation.estimatedTime(path2) == 0);//zero length path
		
	}

}
