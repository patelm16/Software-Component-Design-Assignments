/**
 * @author Meet Patel, patelm16
 *
 */
public class Map {
	
	Obstacles obstacles;
	Destinations destinations;
	SafeZone safeZone;
	
	public void init(Obstacles o, Destinations d, SafeZone sz){
		obstacles = o;
		destinations = d;
		safeZone = sz;
	}
	
	public Obstacles get_obstacles(){
		return obstacles;
	}
	
	public Destinations get_destinations(){
		return destinations;
	}
	
	public SafeZone get_safeZone(){
		return safeZone;
	}
}