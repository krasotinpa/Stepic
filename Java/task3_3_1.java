public class task3_3_1 {

    public static void moveRobot(Robot robot, int toX, int toY) {
        Direction destDir;
        // Определим направление движения по оси X
        destDir = toX - robot.getX() >= 0 ? Direction.RIGHT : Direction.LEFT;
        while (robot.getDirection() != destDir) {
            robot.turnLeft();
            // System.out.println(destDir+" "+robot.getDirection());
        }
        // Двигаемся по оси X
        while (robot.getX() != toX) {
            robot.stepForward();
            // System.out.println(toX+" "+robot.getDirection()+" "+ (toX - robot.getX()));
        }
        // Определим направление движения по оси Y
        destDir = toY - robot.getY() >= 0 ? Direction.UP : Direction.DOWN;
        while (robot.getDirection() != destDir) {
            robot.turnLeft();
            // System.out.println(destDir+" "+robot.getDirection());
        }
        // Двигаемся по оси Y
        while (robot.getY() != toY) {
            robot.stepForward();
            // System.out.println(toY+" "+robot.getDirection()+" "+ (toY - robot.getY()));
        }
    }
    public static void main(String args[]) {
        Robot R = new Robot(1, 8, Direction.UP);
        moveRobot(R, -10, -5);
        System.out.println(R.getX()+" "+R.getY());
    }
}
