import sys
sys.path.insert(0, '../qworld/include')

from drawing import plot_2D_plane, draw_sides, draw_vector, place_text, show_plt

def visualize_vectors(example):
    if example == "example1":
        plot_2D_plane(right=4,up=3,left=-2,down=-2,fsize=(5,5))
        draw_vector(1,2,sides=True,show_name=True,vname="v")
        show_plt()
    elif example == "example2":
        plot_2D_plane(right=5,up=5,left=-3,down=-3,fsize=(6,6))
        draw_vector(2,4,sides=True,show_name=True,vname="2v")
        draw_vector(-1,-2,sides=True,show_name=False,vcolor="g",side_color="g")
        place_text(-3,-2.5,"$-v=(-1,-2)$",tcolor="g")
        show_plt()
    elif example == "example3":
        plot_2D_plane(right=3,up=5,left=-5,down=-3,fsize=(6,6))
        draw_vector(-3,4,sides=True,show_name=False)
        place_text(-2.5,4.2,"$x^2=(-3)^2=9$")
        place_text(-5,2,"$y^2=4^2=16$")
        place_text(-1.43,2.3,"$||u||=\sqrt{(-3)^2+4^2}=\sqrt{25}=5$")
        show_plt()

def dot_product(example):
    if example == "example1":
        plot_2D_plane(right=2,up=2,left=-5,down=-6,fsize=(6,6))
        draw_vector(-4,0,show_name=True,vname="v",lwidth=1.3)
        draw_vector(0,-5,show_name=True,vname="u",lwidth=1.3,vcolor="g")
        show_plt()
    elif example == "example2":
        plot_2D_plane(right=1,up=4,left=-5,down=-5,fsize=(6,6))
        draw_vector(-4,3,show_name=True,vname="v",lwidth=1.3)
        draw_vector(-3,-4,show_name=True,vname="u",lwidth=1.3,vcolor="g")
        show_plt()
    elif example == "example3":
        plot_2D_plane(right=5,up=5,left=-5,down=-5,fsize=(7,7))
        draw_vector(-4,3,show_name=True,vname="v",lwidth=0.8)
        draw_vector(-3,-4,show_name=True,vname="u",lwidth=0.8,vcolor="g")
        draw_vector(4,-3,show_name=True,vname="-v",lwidth=0.8,vcolor="orange")
        draw_vector(3,4,show_name=True,vname="-u",lwidth=0.8,vcolor="c")
        show_plt()
    
def example():
    plot_2D_plane(3,5,-7,-1)

    draw_vector(3,4,sides=True,show_name=False)

    draw_vector(-1,4,show_name=False,sides=True,side_color="g")
    #place_text(1,4.2,"$|u|=\sqrt{3^2+4^2}$")
    place_text(0.5,4.2,"$x^2=3^2=9$")
    place_text(3.2,2,"$y^2=4^2=16$",tcolor="red")
    place_text(3.1,4.1,"$|v|=\sqrt{3^2+4^2}=\sqrt{25}=5$")

    show_plt()