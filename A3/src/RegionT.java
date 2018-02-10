/**
 * @author Meet Patel, patelm16
 * class that creates the region which user will work on
 */
public class RegionT {

	private PointT lower_left;

	private double width;
	
	private double height;

	/**
	 * constructor of class RegionT which creates region using width, height, 
	 * @param p is a PointT object which is the lower left point of the region
	 * @param w is width of region 
	 * @param h is height of region
	 * @throws InvalidRegionException if region is out of bounds
	 */
	public RegionT(PointT p, double w, double h) throws InvalidRegionException {
		if (h < 0 || w < 0 || p.xcrd() + w > Constants.MAX_X || p.ycrd() + h > Constants.MAX_Y)
			throw new InvalidRegionException("Region is out of bounds.");
		lower_left = p;
		width = w;
		height = h;
	}

	/**
	 * function to check if given point, p, is in tolerance of region
	 * @param p is a PointT object 
	 * @return true is point p is in the region and within the tolerance value
	 */
	public boolean pointInRegion(PointT p) {

		double xChange = Math.max(Math.abs(p.xcrd() - (lower_left.xcrd() + width / 2)) - width / 2, 0);
		double yChange = Math.max(Math.abs(p.ycrd() - (lower_left.ycrd() + height / 2)) - height / 2, 0);

		double dist = Math.sqrt(Math.pow(xChange, 2) + Math.pow(yChange, 2));

		return dist <= Constants.TOLERANCE;
	}

}
