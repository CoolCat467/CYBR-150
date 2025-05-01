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

package com.signinapp.signin;

import java.lang.IndexOutOfBoundsException;

public class DaString {
	private String[] values;
	private int size;

	public DaString(int initial_size) {
		this.values = new String[max(1, initial_size)];
		this.size = 0;
	}

	public DaString(){
		this(1);
	}

	private static int min(int a, int b) {
        return (a < b) ? a : b;
    }

    private static int max(int a, int b) {
        return (a > b) ? a : b;
    }

	public String get(int index) throws IndexOutOfBoundsException{
		if (index > this.size){
			throw new IndexOutOfBoundsException();
		}
		return this.values[index];
	}

	public void set(int index, String value) throws IndexOutOfBoundsException{
		// System.out.printf("set index = %d value = %s\n", index, value);
		if (index > this.size){
			// System.out.print("set out of bounds");
			throw new IndexOutOfBoundsException();
		}
		this.values[index] = value;
	}

	private static void copy_entries(int count, String[] old, String[] new_){
		for (int i = 0; i < count; i++){
			new_[i] = old[i];
		}
	}

	private void resize(int new_size){
		String[] new_array = new String[new_size];
		copy_entries(min(this.values.length, new_size), this.values, new_array);
		this.values = new_array;
	}

	public void append(String value){
		int index = this.size;
		if (index >= this.values.length){
			this.resize(this.values.length*2);
		}
		if (index >= this.size){
			this.size += 1;
		}
		try {
			this.set(index, value);
		} catch (IndexOutOfBoundsException exc) {
			System.out.println("unexpected exception happened");
			System.out.println(exc);
		}
	}

	public String[] get_raw(){
		String[] array = new String[this.size];
		copy_entries(this.size, this.values, array);
		return array;
	}

	// private static void print(String[] sequence){
    //     System.out.print("[");
    //     for (int i=0; i<sequence.length; i++){
    //         System.out.printf("\"%s\"", sequence[i]);
    //         if (i < sequence.length - 1){
    //             System.out.print(", ");
    //         }
    //     }
    //     System.out.println("]");
    // }
}
