/**
 * class which does various kinds of calculations on a path
 * @author Meet Patel, patelm16
 *
 */

public class PathCalculation {

	/**
	 * function used to determine total distance of paths
	 * @param p is a PathT objects
	 * @return sum of lengths of piecewise segments that make up the sequence of points in path
	 * @throws InvalidPositionException for an invalid position
	 */
	public static double totalDistance(PathT p) throws InvalidPositionException  {
		double distance = 0;
		for (int i = 0; i < p.size() - 1; i++) {
			distance = distance + (p.getval(i).dist(p.getval(i + 1)));
		}
		return distance;

	}

	/**
	 * function determines total turns made in path p
	 * @param p is a PathT object
	 * @return number of total turns made in path p
	 * @throws InvalidPositionException for an invalid position
	 */
	public static int totalTurns(PathT p) throws InvalidPositionException {
		int turns = 0;
		for (int i = 0; i < p.size() -2; i++){
			if (angle(p.getval(i),p.getval(i+1),p.getval(i+2)) != 0){
				turns = turns + 1;
			}
		}
		return turns;

	}

	/**
	 * finds estimated time of path p
	 * @param p is a PathT object
	 * @return an estimated time to complete path p
	 * @throws InvalidPositionException for an invalid position
	 */
	public static double estimatedTime(PathT p) throws InvalidPositionException {
		return linear_time(p) + angular_time(p);
	}
	
	/**
	 * local function which finds angle between 3 given points
	 * @param p1 is a PointT object
	 * @param p2 is a PointT object
	 * @param p3 is a PointT object
	 * @return angle between all points
	 */
	private static double angle(PointT p1, PointT p2, PointT p3){
		double ux = p2.xcrd() - p1.xcrd();
		double uy = p2.ycrd() - p1.ycrd();
		
		double vx = p3.xcrd() - p2.xcrd();
		double vy = p3.ycrd() - p2.ycrd();
		
		double magU = p1.dist(p2);
		double magV = p2.dist(p3);
		
		double num = ux * vx + uy * vy;
		double den = magU * magV;
		
		return Math.acos(num / den);
	}
	
	/**
	 * local function which finds linear time of path given
	 * @param p is a PathT object
	 * @return linear time of path p
	 * @throws InvalidPositionException for an invalid position
	 */
	private static double linear_time(PathT p) throws InvalidPositionException{
		double linTime = 0;
		for (int i = 0; i < p.size() -1 ; i++){
			linTime += (p.getval(i).dist(p.getval(i+1)))/ Constants.VELOCITY_LINEAR;
		}
		return linTime;
	}
	
	/** 
	 * local function which finds angular time of path given
	 * @param p is a PathT object
	 * @return angular time of path p
	 * @throws InvalidPositionException for an invalid position
	 */
	private static double angular_time(PathT p) throws InvalidPositionException{
		double angTime = 0;
		for (int i = 0; i < p.size() -2 ; i++){
			angTime += (angle(p.getval(i),p.getval(i+1),p.getval(i+2)))/ Constants.VELOCITY_ANGULAR;
		}
		return angTime;
	}

}
