// Copyright (C) 2025  CoolCat467
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <https://www.gnu.org/licenses/>.


public class Final_Java {
    public static void main(String[] args){
        Triangle triangle = new Triangle("pointy hat friend", 3, 4);
        // Triangle triangle = new Triangle();
        System.out.println(triangle);

        Rectangle rectangle = new Rectangle("get rekt kekw", 3, 4);
        System.out.println(rectangle);

        Polygon[] polygons = new Polygon[]{triangle, new Triangle(), rectangle, new Rectangle()};
        print(polygons);
    }

    public static void print(Object[] sequence){
        System.out.print("[");
        for (int i=0; i<sequence.length; i++){
            System.out.printf("%s", sequence[i].toString());
            if (i < sequence.length - 1){
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }

    public static void print(String[] sequence){
        System.out.print("[");
        for (int i=0; i<sequence.length; i++){
            System.out.printf("\"%s\"", sequence[i]);
            if (i < sequence.length - 1){
                System.out.print(", ");
            }
        }
        System.out.println("]");
    }
}
