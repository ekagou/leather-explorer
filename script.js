document.addEventListener("DOMContentLoaded", async () => {
    const galleryContainer = document.getElementById("lightgallery");

    if (galleryContainer) {
        try {
            const response = await fetch('/api/photos');
            const photos = await response.json();
            
            photos.forEach(photo => {
                const anchor = document.createElement("a");
                anchor.className = "gallery-item";
                anchor.href = photo.full;
                anchor.setAttribute("data-src", photo.full);
                
                const img = document.createElement("img");
                img.src = photo.thumb;
                img.loading = "lazy";
                
                const overlay = document.createElement("div");
                overlay.className = "gallery-overlay";
                
                const span = document.createElement("span");
                span.textContent = "VIEW IMAGE";
                
                overlay.appendChild(span);
                anchor.appendChild(img);
                anchor.appendChild(overlay);
                
                galleryContainer.appendChild(anchor);
            });
            
            // Initialize LightGallery after DOM elements are appended
            lightGallery(galleryContainer, {
                plugins: [lgZoom, lgThumbnail, lgShare],
                speed: 500,
                licenseKey: '0000-0000-000-0000', // free use
                download: false,
                mode: 'lg-fade',
                mobileSettings: {
                    controls: true,
                    showCloseIcon: true,
                },
                facebook: false,
                twitter: false,
                pinterest: false,
                share: true,
                additionalShareOptions: [
                    {
                        id: 'whatsapp',
                        label: 'WhatsApp',
                        url: 'https://wa.me/?text=' + encodeURIComponent(window.location.href),
                        icon: 'lg-icon-whatsapp' 
                    }
                ]
            });
        } catch (error) {
            console.error("Error loading photos:", error);
        }
    }
});
