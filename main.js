// Init swiper when present
document.addEventListener('DOMContentLoaded', function(){
  const el = document.querySelector('.events-swiper');
  if(el){
    new Swiper('.events-swiper', {
      slidesPerView: 1,
      spaceBetween: 12,
      loop: true,
      autoplay: { delay: 4000, disableOnInteraction: false },
      pagination: { el: '.swiper-pagination', clickable: true }
    });
  }
});
