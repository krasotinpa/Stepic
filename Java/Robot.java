public class Robot {
    private int x=0;
    private int y=0;
    private Direction direction = Direction.UP;

    public Robot(int x, int y, Direction direction) {
        this.x = x;
        this.y = y;
        this.direction = direction;
    }

    public Direction getDirection() {
        // текущее направление взгляда
        return(direction);
    }

    public int getX() {
        // текущая координата X
        return(x);
    }
    

    public int getY() {
        // текущая координата Y
        return(y);
    }

    public void turnLeft() {
        // повернуться на 90 градусов против часовой стрелки
        switch (getDirection()){
            default:
            case DOWN:
                direction = Direction.RIGHT;
                break;
            case UP:
                direction = Direction.LEFT;
                break;
            case RIGHT:
                direction = Direction.UP;
                break;
            case LEFT:
                direction = Direction.DOWN;
        }
    }

    public void turnRight() {
        // повернуться на 90 градусов по часовой стрелке
        switch (getDirection()){
            default:
            case DOWN:
                direction = Direction.LEFT;
                break;
            case UP:
                direction = Direction.RIGHT;
                break;
            case RIGHT:
                direction = Direction.DOWN;
                break;
            case LEFT:
                direction = Direction.UP;
        }
    }

    public void stepForward() {
        // шаг в направлении взгляда
        // за один шаг робот изменяет одну свою координату на единицу
        switch (getDirection()){
            default:
            case DOWN: y--;
                break;
            case UP: y++;
                break;
            case RIGHT: x++;
                break;
            case LEFT: x--;
        }
    }
}
