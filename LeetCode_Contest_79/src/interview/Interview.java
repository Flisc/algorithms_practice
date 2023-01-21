package interview;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Interview {

    public static void main(String[] args) {

        System.out.println("Minimum time = " + minTimeToVisitAllPoints(new int[][]{
                new int[]{1, 1},
                new int[]{3, 4},
                new int[]{-1, 0},
                new int[]{-2, 1}
        }) + " seconds");

        System.out.println("Minimum time = " + minTimeToVisitAllPoints(new int[][]{
                new int[]{3, 2},
                new int[]{-2, 2}
        }) + " seconds");
    }

    private static int minTimeToVisitAllPoints(int[][] points) {
        int counter = 0;
        List<Pair> pairs = new ArrayList<>();
        for (int[] point : points) {
            pairs.add(new Pair(false, point[0], point[1]));
        }
        int i = 0;
        Pair currentPoint = new Pair();
        Pair nextPoint = new Pair();

        while (!checkStatus(pairs)) {
            if (i == 0) {
                currentPoint = pairs.get(i);
                currentPoint.visited = true;
            }
            if (pairs.contains(currentPoint)) {
                pairs.get(pairs.indexOf(currentPoint)).visited = true;
            }
            if (checkStatus(pairs)) break;
            nextPoint = getNextForDirection(currentPoint, getFirstUnvisited(pairs));
            System.out.println(++counter + ". " +
                    currentPoint.toString() +
                    "\n \t| " +
                    "\n\tv");
            if (pairs.get(pairs.size() - 1).equals(nextPoint)) {
                System.out.println(++counter + ". " +
                        nextPoint.toString());
                return --counter;
            }
            currentPoint = nextPoint;
            i++;
        }
        return counter;
    }

    private static class Pair {
        public boolean visited;
        public int x;
        public int y;

        public Pair(boolean visited, int x, int y) {
            this.visited = visited;
            this.x = x;
            this.y = y;
        }

        public Pair() {
        }

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Pair)) return false;
            Pair pair = (Pair) o;
            return x == pair.x && y == pair.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }

        @Override
        public String toString() {
            return "{" +
                    x + ", " +
                    y +
                    '}';
        }
    }

    private static Pair getNextForDirection(Pair currentPoint, Pair destination) {
        if (destination.x > currentPoint.x && destination.y > currentPoint.y) {
            //right up
            return new Pair(currentPoint.x + 1, currentPoint.y + 1);
        } else if (destination.x > currentPoint.x && destination.y == currentPoint.y) {
            // right
            return new Pair(currentPoint.x + 1, currentPoint.y);
        } else if (destination.x > currentPoint.x && destination.y < currentPoint.y) {
            // right down
            return new Pair(currentPoint.x + 1, currentPoint.y - 1);
        } else if (destination.x == currentPoint.x && destination.y < currentPoint.y) {
            //  down
            return new Pair(currentPoint.x, currentPoint.y - 1);
        } else if (destination.x < currentPoint.x && destination.y < currentPoint.y) {
            //  down left
            return new Pair(currentPoint.x - 1, currentPoint.y - 1);
        } else if (destination.x == currentPoint.x && destination.y > currentPoint.y) {
            //  up
            return new Pair(currentPoint.x, currentPoint.y + 1);
        } else if (destination.x < currentPoint.x && destination.y == currentPoint.y) {
            // left
            return new Pair(currentPoint.x - 1, currentPoint.y);
        } else if (destination.x < currentPoint.x && destination.y > currentPoint.y) {
            // left up
            return new Pair(currentPoint.x - 1, currentPoint.y + 1);
        }
        return null;
    }

    private static boolean checkStatus(List<Pair> points) {
        return points.stream().allMatch(pair -> pair.visited == true);
    }

    private static Pair getFirstUnvisited(List<Pair> pairs) {
        return pairs.stream().filter(pair -> pair.visited == false).findFirst().orElse(null);
    }

}
