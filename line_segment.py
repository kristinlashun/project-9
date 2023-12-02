# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: December 1st, 2023
# Description: This program defines two classes 'Point' and 'LineSegment' to represent geometric points and line segments. It includes methods to calculate distance, length, slope, and check parallelism.

import math

class Point:
    """Class to represent a point in a 2D space."""
    def __init__(self, x_coord, y_coord):
        """Initialize the point with x and y coordinates."""
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        """Return the x coordinate of the point."""
        return self._x_coord

    def get_y_coord(self):
        """Return the y coordinate of the point."""
        return self._y_coord

    def distance_to(self, other):
        """Calculate the Euclidean distance to another point."""
        return math.sqrt((self._x_coord - other.get_x_coord())**2 + (self._y_coord - other.get_y_coord())**2)

class LineSegment:
    """Class to represent a line segment in a 2D space defined by two points."""
    def __init__(self, endpoint_1, endpoint_2):
        """Initialize the line segment with two endpoints."""
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        """Return the first endpoint of the line segment."""
        return self._endpoint_1

    def get_endpoint_2(self):
        """Return the second endpoint of the line segment."""
        return self._endpoint_2

    def length(self):
        """Calculate the length of the line segment."""
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self):
        """Calculate the slope of the line segment."""
        try:
            return (self._endpoint_2.get_y_coord() - self._endpoint_1.get_y_coord()) / (self._endpoint_2.get_x_coord() - self._endpoint_1.get_x_coord())
        except ZeroDivisionError:
            return math.inf  # Slope is infinite for vertical line segments

    def is_parallel_to(self, other):
        """Check if the line segment is parallel to another line segment."""
        return math.isclose(self.slope(), other.slope(), abs_tol=1e-9)

