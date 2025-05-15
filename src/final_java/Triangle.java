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

import java.lang.Math;

public class Triangle extends Polygon {
    private int height;
    private int length;

    public Triangle(){
        this("untitled", 0, 0);
    }

    public Triangle(String name, int height, int length){
        super(name, 3);
        this.setHeight(height);
        this.setLength(length);
    }

    public double getArea(){
        return (this.getHeight() * this.getLength()) / 2.0;
    }

    public double getHypotenuse(){
        return Math.hypot(this.getHeight(), this.getLength());
    }

    public double getPerimeter(){
        return (this.getHeight() + this.getLength()) + this.getHypotenuse();
    }

    public void setHeight(int height){
        this.height = height;
    }
    public void setLength(int length){
        this.length = length;
    }
    public int getHeight(){
        return this.height;
    }
    public int getLength(){
        return this.length;
    }
    public String toString(){
        String previous = super.toString();
        previous = previous.substring(0, previous.length() - 1);
        return previous + ", height=" + this.getHeight() + ", length=" + this.getLength() + ")";
    }
}
