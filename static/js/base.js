// const $dropdown = $(".dropdown");
// const $dropdownToggle = $(".dropdown-toggle");
// const $dropdownMenu = $(".dropdown-menu");
// const showClass = "show";

// if (this.matchMedia("(min-width: 768px)").matches) {
//   $dropdown.hover(
//     function() {
//       const $this = $(this);
//       $this.addClass(showClass);
//       $this.find($dropdownToggle).attr("aria-expanded", "true");
//       $this.find($dropdownMenu).addClass(showClass);
//     },
//     function() {
//       const $this = $(this);
//       $this.removeClass(showClass);
//       $this.find($dropdownToggle).attr("aria-expanded", "false");
//       $this.find($dropdownMenu).removeClass(showClass);
//     }
//   );
// } else {
//   $dropdown.off("mouseenter mouseleave");
// }

$("#top-sale .owl-carousel").owlCarousel({
  loop:true,
  nav:true,
  dots:false,
  responsive: {
      0:{
          items:1
      },
      600:{
          items:3
      },
      1000:{
          items:5
      }
  }
})

