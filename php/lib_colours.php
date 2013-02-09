<?php

	########################################################################

	function colours_load_palette($path){

		$fh = fopen($path, 'r');
		$txt = fread($fh, filesize($path));

		$data = json_decode($txt, "as hash");
		return $data;
	}

	########################################################################

	function colours_closest_colour($hex, &$palette){

		list ($r, $g, $b) = colours_hex_to_rgb($hex);

		$min_colours = array();

		foreach ($palette['colours'] as $palette_hex => $details){

			list($rc, $gc, $bc) = colours_hex_to_rgb($palette_hex);

			$rd = pow(($rc - $r), 2);
			$gd = pow(($gc - $g), 2);
			$bd = pow(($bc - $b), 2);

			$key = $rd + $gd + $bd;
			$min_colours[ $key ] = $details;
		}	

		$idx = min(array_keys($min_colours));
		$details = $min_colours[$idx];

		$closest_name = $details['name'];
		$closest_hex = colours_name_to_hex($palette, $closest_name);

		return array($closest_hex, $closest_name);
	}

	########################################################################

	function colours_name_to_hex(&$palette, $name){

		foreach ($palette['colours'] as $hex => $details){
			if ($details['name'] == $name){
				return $hex;
			}
		}

		return null;
	}

	########################################################################

	function colours_hex_to_rgb($hex){

		$hex = str_replace("#", "", $hex);
		$r = hexdec(substr($hex, 0, 2));
		$g = hexdec(substr($hex, 2, 2));
		$b = hexdec(substr($hex, 4, 2));

		return array($r, $g, $b);
	}

	########################################################################

	function colours_rgb_to_hex($rgb){

		$hex = "#";
		$hex .= str_pad(dechex($rgb[0]), 2, "0", STR_PAD_LEFT);
		$hex .= str_pad(dechex($rgb[1]), 2, "0", STR_PAD_LEFT);
		$hex .= str_pad(dechex($rgb[2]), 2, "0", STR_PAD_LEFT);

		return $hex;
	}

	########################################################################

	# the end
