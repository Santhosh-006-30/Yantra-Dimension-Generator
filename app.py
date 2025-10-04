from flask import Flask, render_template, request
import math
from math import radians, tan, pi

app = Flask(__name__)

# ----------------- Instrument Models -----------------

def samrat_yantra(lat_deg, base_radius_m=10.0):
    lat = radians(lat_deg)
    R = base_radius_m
    H = R * tan(lat)
    sloping_face_length = math.hypot(R, H)
    return {
        'type': 'Samrat Yantra',
        'base_full_width_m': round(2 * R, 2),
        'gnomon_height_H_m': round(H, 2),
        'sloping_face_length_m': round(sloping_face_length, 2)
    }

def rama_yantra(lat_deg, outer_radius_m=6.0):
    inner_R = max(0.6 * outer_radius_m, outer_radius_m - 1.0)
    return {
        'type': 'Rama Yantra',
        'outer_radius_m': outer_radius_m,
        'inner_radius_m': round(inner_R, 2)
    }

def digamsa_yantra(lat_deg, circle_radius_m=5.0):
    arc_length = circle_radius_m * radians(1)  # per degree
    return {
        'type': 'Digamsa Yantra',
        'radius_m': circle_radius_m,
        'arc_length_per_deg_m': round(arc_length, 3)
    }

def bhitti_yantra(lat_deg, wall_height_m=6.0):
    scale = min(wall_height_m, 0.01 / (pi/180))
    return {
        'type': 'Bhitti Yantra',
        'wall_height_m': wall_height_m,
        'recommended_vertical_length_for_1deg_m': round(scale, 2)
    }

def golayantra_armillary(lat_deg, ring_outer_radius_m=3.0):
    return {
        'type': 'Golayantra Yantra',
        'outer_ring_radius_m': ring_outer_radius_m,
        'ecliptic_tilt_deg': 23.44
    }

def generate_report(lat, lon):
    return [
        samrat_yantra(lat),
        rama_yantra(lat),
        digamsa_yantra(lat),
        bhitti_yantra(lat),
        golayantra_armillary(lat)
    ]

# ----------------- Routes -----------------

@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    lat, lon = None, None
    if request.method == "POST":
        lat = float(request.form.get("lat"))
        lon = float(request.form.get("lon"))
        report = generate_report(lat, lon)
    return render_template("index.html", report=report, lat=lat, lon=lon)

if __name__ == "__main__":
    app.run(debug=True)
